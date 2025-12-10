import requests

methods = ["GET", "POST", "PUT", "DELETE"]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# Задание 1.
print("1. Запрос любого типа без параметра method")
response = requests.get(url)

if response.status_code == 200:
    print("Успешно: ", response.status_code)
    print(response.text)
else:
    print("Ошибка:", response.status_code)
    print(response.text)

# Задание 2.
print("2. Запрос, который делает запрос не из списка (HEAD)")
response = requests.head(url)

if response.status_code == 200:
    print(response.status_code)
    print(response.text)
else:
    print(response.status_code)
    print(response.text)

# Задание 3.
print("3. Запрос с правильным значением method")

response = requests.get(url, params={"method":"GET"})
response1 = requests.post(url, data={"method":"POST"})
response2 = requests.put(url, data={"method":"PUT"})
response3 = requests.delete(url, data={"method":"DELETE"})

print("GET: ", response.text, response.status_code)
print("POST: ", response1.text, response1.status_code)
print("PUT: ", response2.text, response2.status_code)
print("DELETE: ", response3.text, response3.status_code)

# Задание 4

for method in methods:
    for param in methods:
            if method == "GET":
                response = requests.get(url, params={"method": param})
            else:
                response = requests.request(method, url, data={"method": param})

            if method == param:
                print(method, param, response.text, response.status_code)
            else:
                print(method, param, response.text, response.status_code)



