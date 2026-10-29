class Assistant:
    def __init__(self, instructions: str, model, client):
        self.model = model
        self.instructions = instructions
        self.client = client
        self.previous_response_id_map = {}

    def __call__(self, input_: str, session_id: str='default'):
        # Получите ID предыдущего сообщения для данной сессии
        previous_response_id = self.previous_response_id_map.get(session_id, None)

        # Сформируйте ответ модели
        res = self.client.responses.create(
            model = self.model,
            store = True,
            previous_response_id = previous_response_id,
            instructions = self.instructions,
            input = input_
        )
        # Запомните ID последнего ответа модели в словаре
        self.previous_response_id_map[session_id] = res.id
        return res.output_text
