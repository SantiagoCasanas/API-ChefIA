# API-ChefIA
In the kitchen, we often face the challenge of deciding what to cook with the ingredients available in our fridge. Sometimes we come across ingredients that we don't know how to use or we would like to try new recipes but don't know where to start. In addition, it can be a bit difficult to remember all the recipes we know or to search for new recipes that suit the ingredients we have on hand.

FoodLens is a cooking app that uses Amazon Rekognition to automatically identify foods in an image taken by the user. With this feature, users can take a picture of available ingredients and quickly receive recipes and cooking suggestions based on those ingredients. In addition, the application integrates the power of OpenAI to offer personalized and creative recommendations.

## To run the API locally you will need to follow the steps below:

1. Clone the repository to the desired location.
2. Open a terminal of your choice in the folder of the cloned repository. (For the instructions it will be 
assumed that you used Git Bash).
3. Create a virtual environment using:
```
python -m venv venv
```
4. Activate the virtual environment:
```
source venv/Scripts/activate
```
5. Install the requirements using:
```
pip install -r requirements.txt
```
6. Create an .env file in the repository root that has the following structure:
```
openai_key = Your openai key
origins = [
    "http://localhost",
    "http://localhost:8080",
    "127.0.0.1"
]
```
Adding in origins the addresses from which you want to allow requests, or in case you want to allow any address
```
origins = [
    "*"
]
```
7. Execute the following command to run the API:
```
uvicorn main:app --reload
```
8. Access the following path to see the available endpoint's and their parameters
```
http://127.0.0.1:8000/docs
```



En la cocina, a menudo nos enfrentamos al desafío de decidir qué cocinar con los ingredientes disponibles en nuestra nevera. A veces nos encontramos con ingredientes que no sabemos cómo utilizar o nos gustaría probar nuevas recetas pero no sabemos por dónde empezar. Además, puede ser un poco difícil recordar todas las recetas que conocemos o buscar nuevas recetas que se adapten a los ingredientes que tenemos a la mano.

FoodLens es una aplicación de cocina que utiliza Amazon Rekognition para identificar automáticamente los alimentos en una imagen tomada por el usuario. Con esta función, los usuarios pueden tomar una foto de los ingredientes disponibles y recibir rápidamente recetas y sugerencias de cocina basadas en esos ingredientes. Además, la aplicación integra el poder de OpenAI para ofrecer recomendaciones personalizadas y creativas.

## Para ejecutar la API de manera local deberá seguir los siguientes pasos:
1. Clone el repositorio en la ubicación deseada.
2. Abra una terminal de su preferencia en la carpeta del repositorio clonado. (Para las instrucciones se supondrá
que usó Git Bash)
3. Cree un ambiente virtual usando:
```
python -m venv venv
```
4. Active el ambiente virtual:
```
source venv/Scripts/activate
```
5. Instale los requerimientos usando:
```
pip install -r requirements.txt
```
6. Cree un archivo .env en la raíz del repositorio que tenga la siguiente estructura:
```
openai_key = Tu key de openai
origins = [
    "http://localhost",
    "http://localhost:8080",
    "127.0.0.1"
]
```
Agregando en origins las direcciones desde las cuales desea permitir las peticiones, o en caso de desear permitir cualquier dirección
```
origins = ["*"]
```
En caso de desear permitir cualquier dirección.

7. Ejecute el siguiente comando para correr la API:
```
uvicorn main:app --reload
```
8. Acceda a la siguiente ruta para ver los endpoint's disponibles y sus parametros
```
http://127.0.0.1:8000/docs
```