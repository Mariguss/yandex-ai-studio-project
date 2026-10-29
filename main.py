import openai
from openai import OpenAI

from assistant import Assistant
from config import settings

instructions = """
Ты — профессиональный фитнес-ассистент. Отвечай как энергичный молодой человек 
со спортивным задором. Говори как человек, короткими фразами, избегая 
перечислений и списков.
"""

client = OpenAI(
   base_url = "https://ai.api.cloud.yandex.net/v1",
   api_key = settings.ai.api_key,
   project = settings.ai.folder_id
)

model = f"gpt://{settings.ai.folder_id}/gpt-oss-120b"

assistant = Assistant(
    instructions=instructions,
    model=model,
    client=client,
)

print(assistant("Привет! С чего ты порекомендуешь начать тренировки в зале?"))

print(assistant("Я хочу похудеть!"))
