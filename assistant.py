import json

from tools.exersise import log_exercise
from tools.exersise_description import log_exercise_tool


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
            input = input_,
            tools=[log_exercise_tool]
        )
        # Запомните ID последнего ответа модели в словаре
        self.previous_response_id_map[session_id] = res.id
        # Проверка, есть ли вызов функции в ответе
        for output_item in res.output:
            if output_item.type == "function_call":
                # Извлечение имени функции и аргументы
                function_name = output_item.name
                arguments_str = output_item.arguments  # Это строка в формате JSON

                print(f"Модель запросила вызов функции: {function_name}")
                print(f"С аргументами: {arguments_str}")

                # Парсинг аргументов из JSON-строки в словарь Python
                arguments = json.loads(arguments_str)

                # Вызов функции с аргументами
                if function_name == "log_exercise":
                    result = log_exercise(**arguments)
                    print(f"Функция выполнена, результат: {result}")

                    # Формирование текстового сообщения с результатом
                    result_message = f"Результат выполнения функции {function_name}: {json.dumps(result, ensure_ascii=False)}"

                    # Отправка результата обратно модели
                    follow_up = self.client.responses.create(
                        model=self.model,
                        store=True,
                        previous_response_id=res.id,
                        input=result_message
                    )

                    # Вывод финальный ответ модели пользователю
                    return follow_up.output_text
        else:
            return res.output_text
