import os
import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

GENDER = "Male"
WEIGHT_KG = "80"
HEIGHT_CM = "189"
AGE = 45

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = f"https://api.sheety.co/{os.environ.get('SHEETY')}/workoutTracking/workouts"

input_text = input("Wich exercise did you do? ")

headers = {"x-app-id": APP_ID, "x-app-key": APP_KEY, "x-remote-user": "0"}

parameters = {"query": input_text, "gender": GENDER, "weight_kg": WEIGHT_KG, "height_cm": HEIGHT_CM, "age": AGE}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {"Authorization": f"Bearer {os.environ.get('TOKEN')}"}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
