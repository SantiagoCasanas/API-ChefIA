import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from utils.models import Context, Response, IngredientResponse
from utils.utils import get_recipe_openai, get_list_ingredients

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación FastAPI
app = FastAPI()

# Obtener los orígenes permitidos desde las variables de entorno
origins = os.getenv('origins')

# Configurar el middleware CORS para permitir solicitudes desde los orígenes especificados
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint para obtener ingredientes a partir de una imagen
@app.post("/get-ingredients")
async def read_item(file: UploadFile = File(...)):
    try:
        # Leer los bytes de la imagen
        source_bytes = await file.read()
        # Obtener la lista de ingredientes desde la imagen
        results = get_list_ingredients(source_bytes)
        # Crear una respuesta JSON con la lista de ingredientes
        return JSONResponse(content=IngredientResponse(ingredients=results).dict(), status_code=200)
    except FileNotFoundError:
        # Manejar el caso en que el archivo no se encuentra
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

# Endpoint para obtener una receta utilizando los ingredientes proporcionados
@app.post("/get-recipe", response_model=Response)
def read_item(context: Context) -> Response:
    # Obtener la receta utilizando los ingredientes proporcionados
    results = get_recipe_openai(context)
    # Crear una respuesta con la receta
    response = Response(message=results)
    return response
