import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()



APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
SHEETY_ENDPOINT = os.environ.get('SHEETY_API')
AUTH = os.environ.get('AUTH')

today_date = datetime.today().strftime('%d/%m/%Y')
current_hour = datetime.now().strftime('%H:%M:%S')
exercise = input('Tell me which exercises you did: ')
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
params = {
    'query':exercise,
    'gender':'male',
    'weight_kg':'81',
    'height_cm':'185',
    'age':'25'
}
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Authorization': AUTH
}

exercise_response = requests.post(url=exercise_endpoint, json=params, headers=headers)
exercise_data = exercise_response.json()['exercises']

for object in exercise_data:
    sheety_params = {
        'workout':{
            'date':today_date,
            'time':current_hour,
            'exercise':object['name'].title(),
            'duration':object['duration_min'],
            'calories':object['nf_calories'],
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=headers)
    print(response.status_code,response.text)
    