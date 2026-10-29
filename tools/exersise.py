import uuid

from datetime import datetime

# Простое хранилище данных в памяти
exercises_db = {}


def log_exercise(exercise_name, sets, reps, weight=None, date=None):
    """
    Записывает информацию о выполненном упражнении в журнал тренировок

    Args:
        exercise_name (str): Название упражнения
        sets (int): Количество подходов
        reps (int): Количество повторений в каждом подходе
        weight (float, optional): Вес в кг
        date (str, optional): Дата тренировки в формате YYYY-MM-DD

    Returns:
        dict: Информация о записи с уникальным ID
    """
    # Генерируем уникальный ID для записи
    record_id = str(uuid.uuid4())

    # Устанавливаем текущую дату, если не указана
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')

    # Создаём запись
    record = {
        "id": record_id,
        "exercise": exercise_name,
        "sets": sets,
        "reps": reps,
        "weight": weight,
        "date": date
    }

    # В реальном приложении здесь был бы код для сохранения в базу данных
    # Для примера просто сохраняем в памяти
    if 'exercise_log' not in exercises_db:
        exercises_db['exercise_log'] = []

    exercises_db['exercise_log'].append(record)

    return {
        "status": "success",
        "message": f"Упражнение '{exercise_name}' успешно записано",
        "record_id": record_id
    }
