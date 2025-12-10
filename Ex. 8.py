import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url).json()
token = response['token']
print(requests.get(url, params={'token': token}).json())

time.sleep(response['seconds'])

result = requests.get(url, params={'token': token}).json()
print(result)

if result['status'] == 'Job is ready':
    print(result['result'])
else:
    print('Job is not ready')