from openai import OpenAI
from .config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_lesson_content(class_name, subject, topic, lesson_type, extra_prompt):

    prompt = f"""
    Создай урок по ГОСО РК и приказу 130.

    Класс: {class_name}
    Предмет: {subject}
    Тема: {topic}
    Тип: {lesson_type}
    Дополнительно: {extra_prompt}

    45 минут.
    Добавить:
    - 7 ценностей
    - физ.минутку
    - действия учеников с ООП
    - критерии оценивания
    - 10 слайдов
    - рабочий лист 2 варианта
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content