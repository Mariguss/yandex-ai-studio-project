# Описание функции для Responses API

log_exercise_tool = {
    "type": "function",
    "name": "log_exercise",
    "description": "Записывает информацию о выполненном упражнении в журнал тренировок",
    "parameters": {
        "type": "object",
        "properties": {
            "exercise_name": {
                "type": "string",
                "description": "Название упражнения"
            },
            "sets": {
                "type": "integer",
                "description": "Количество подходов"
            },
            "reps": {
                "type": "integer",
                "description": "Количество повторений в каждом подходе"
            },
            "weight": {
                "type": "number",
                "description": "Вес в кг (если применимо)"
            },
            "date": {
                "type": "string",
                "description": "Дата тренировки в формате YYYY-MM-DD (если не указана, используется сегодняшняя дата)"
            }
        },
        "required": ["exercise_name", "sets", "reps"]
    }
}
