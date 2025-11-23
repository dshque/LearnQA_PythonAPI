import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1. Создаем задачу
response = requests.get(url)
json_response = response.json()
print("Ответ при создании задачи:", json_response)

token = json_response["token"]
seconds = json_response["seconds"]
print(f"Token: {token}, Seconds: {seconds}")

# 2. Проверяем статус до готовности
response_with_token = requests.get(url, params={"token": token})
json_status = response_with_token.json()
print("Статус до ожидания:", json_status)

if "status" in json_status and json_status["status"] == "Job is NOT ready":
    print("Статус корректен: задача еще не готова")
else:
    print("Ошибка: неправильный статус")

# 3. Ждем нужное время
print(f"Ждем {seconds} секунд...")
time.sleep(seconds)

# 4. Проверяем статус после ожидания
response_after_wait = requests.get(url, params={"token": token})
json_result = response_after_wait.json()
print("Статус после ожидания:", json_result)

if "status" in json_result and json_result["status"] == "Job is ready":
    print("Статус корректен: задача готова")
    if "result" in json_result:
        print(f"Результат получен: {json_result['result']}")
    else:
        print("Ошибка: результат отсутствует")
else:
    print("Ошибка: неправильный статус")