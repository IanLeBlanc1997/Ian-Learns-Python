import requests 
from datetime import datetime

#date time setup
today = datetime.now()
year = today.year
month = today.month
day = today.day

#exercise entry and response
exercise_api_key = '021aa3d694a7e623f462d170368e9897'
exercise_app_id = 'a0aa816b'
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_headers = {'Content-Type':'application/json','x-app-id':exercise_app_id,'x-app-key': exercise_api_key}
exercise = input("What exercise have you done?\n")
exercise_parameters = {'weight_kg':66,'height_cm':160,'age':27,'query':exercise}
exercise_response = requests.post(url=exercise_endpoint,headers=exercise_headers,json=exercise_parameters)

#data parsing of exercise response and datetime variable assignment
workout_result = exercise_response.json()
exercise = workout_result['exercises'][0]['name']
duration = workout_result['exercises'][0]['duration_min']
calories = workout_result['exercises'][0]['nf_calories']
date = f'{year}/{month}/{day}'
time = datetime.now().strftime("%H:%M:%S")

#sheet update
sheetyUN = 'automobilemusic@gmail.com'
sheet_endpoint = 'https://api.sheety.co/7130b0d4939d4c449510184247cbd134/workoutApiTracker/sheet1'
sheet_parameters = {'sheet1':{'date':date,'time':time,"exercise":exercise,"duration":duration,"calories":calories}}

sheet_response = requests.post(url=sheet_endpoint,json=sheet_parameters)


