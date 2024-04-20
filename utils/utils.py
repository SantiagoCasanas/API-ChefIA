import os
import boto3
from dotenv import load_dotenv
from .models import Context
import openai

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene las claves de la API de OpenAI y las credenciales de AWS desde las variables de entorno
api_key = os.getenv('openai_key')
access_key = os.getenv('access_key_aws_rekognition')
secret_access_key = os.getenv('secret_access_key__aws_rekognition')

# Configura la API de OpenAI con la clave proporcionada
openai.api_key = api_key

# Crea una sesión de AWS utilizando las credenciales proporcionadas
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    region_name='us-east-2'
)

# Crea un cliente para Amazon Rekognition
client = session.client('rekognition')

def filter_ingredients(context: Context, model="gpt-3.5-turbo-16k") -> str:
    """
    Filtra los ingredientes de cocina de una lista de objetos en inglés
    y los devuelve en español separados por comas.

    Args:
        context (Context): El contexto que contiene la lista de ingredientes en inglés.
        model (str): El modelo de OpenAI a utilizar para el filtrado.

    Returns:
        str: Una cadena que contiene los ingredientes de cocina en español separados por comas.
    """
    prompt = f'''usando esta lista de objetos en inglés: {context}
filtra los que sean realmente ingredientes de cocina, vegetales, frutas, sazonadores, salsas, tambien
carnes de todo tipo o nombres de animales que se puedan comer, y todas las demas que puedas interpretar 
como un posible ingrediente para realizar una receta a partir de estos acorde a la lista y devuelvemelos en espanol separados por comas, asi: 
ingrediente1, ingrediente2
Sin ningun otro texto, solo los ingredientes'''

    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens=700,
        n=1
    )
    answer = response.choices[0].message
    if answer:
        message = answer.content
    else:
        message = "Sin respuesta"
    return message

def get_list_ingredients(source_bytes: bytes):
    """
    Obtiene una lista de ingredientes a partir de una imagen utilizando Amazon Rekognition.

    Args:
        source_bytes (bytes): Los bytes de la imagen a analizar.

    Returns:
        str: Una cadena que contiene los ingredientes detectados en la imagen.
    """
    detect_objects = client.detect_labels(Image={'Bytes': source_bytes})
    list_ingredients = [label['Name'] for label in detect_objects['Labels']]
    print(list_ingredients)
    ingredients = filter_ingredients(list_ingredients)
    print(ingredients)
    return ingredients

def get_recipe_openai(context: Context, model="gpt-3.5-turbo-16k") -> str:
    """
    Obtiene una receta utilizando los ingredientes proporcionados utilizando OpenAI.

    Args:
        context (Context): El contexto que contiene los ingredientes en inglés.
        model (str): El modelo de OpenAI a utilizar para generar la receta.

    Returns:
        str: Una cadena que contiene la receta generada.
    """
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
        max_tokens=700,
        n=1
    )
    answer = response.choices[0].message
    if answer:
        message = answer.content
    else:
        message = "Sin respuesta"
    return message
