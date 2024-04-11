import openai
import os

from dotenv import load_dotenv

from .models import Context

load_dotenv()

api_key = os.getenv('openai_key')
openai.api_key = api_key

def ask_open_ai(context:Context, model="gpt-3.5-turbo-16k")->str:
    prompt = f'''usando estos ingredientes: {context.ingredients}
dame una receta rápida y fácil de preparar, incluyendo sus instrucciones,
tiempos, y es obligatoria una lista con su información nutricional, el calcio, vitaminas,
todas estas cosas que puedes contarme. tratando de no extenderte demasiado.
Responde siempre en español, sin importar el idioma de los ingredientes'''

    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens= 700,
        n=1
    )
    answer = response.choices[0].message
    if answer:
        message = answer.content
    else:
        message = "Sin respuesta"
    return message