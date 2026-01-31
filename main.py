import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app_id = os.environ["APP_ID"]
app_key = os.environ["API_KEY"]

link = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

queries = input("Tell me which excercises you did: ")
queries = queries.split(" and ")

headers = {
    "x-app-id" : app_id,
    "x-app-key" : app_key,
}

exercises = []

for query in queries:

    parameters = {
        "query" : query,
    }
    response = requests.post(url=link, json=parameters, headers=headers)

    exercise = response.json()["exercises"][0]

    exercises.append(exercise)


today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

sheety_url = os.environ["SHEET_ENDPOINT"]

sheety_headers = {
    "Bearer" : os.environ["BEARER"]
}

for exercise in exercises:
    sheety_parameters = {
        "workout" : {
            "date" : date,
            "time" : time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_url, json=sheety_parameters, headers=sheety_headers)

