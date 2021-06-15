import requests

APP_ID = YOUR APP ID
API_KEY = YOUR API KEY

GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
input_text = input("Wich exercise did you do? ")

headers = {"x-app-id": APP_ID, "x-app-key": APP_KEY, "x-remote-user": "0"}

parameters = {"query": input_text, "gender": GENDER, "weight_kg": WEIGHT_KG, "height_cm": HEIGHT_CM, "age": AGE}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

print(result)
