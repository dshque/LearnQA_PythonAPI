import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1 пункт.
print("1. HTTP-запрос любого типа без передачи параметров (POST).")

response = requests.post(url)

print(response.text)

# 2 пункт.
print("\n2. HTTP-запрос не из списка (HEAD).")

response = requests.head(url)

print(response.text)

# 3 пункт.
print("\n3. HTTP-запросы с правильным значением method.")

response = requests.get(url, params={"method":"GET"})
response1 = requests.post(url, data={"method":"POST"})
response2 = requests.put(url, data={"method":"PUT"})
response3 = requests.delete(url, data={"method":"DELETE"})

print("GET: ", response.text)
print("POST: ", response1.text)
print("PUT: ", response2.text)
print("DELETE: ", response3.text)

# 4 пункт.
print("\n4. GET, POST, PUT, DELETE с разными параметрами.")
# 4.1. GET
print("4.1. GET-запрос")
response = requests.get(url, params={"method":"GET"})
response1 = requests.get(url, params={"method":"POST"})
response2 = requests.get(url, params={"method":"PUT"})
response3 = requests.get(url, params={"method":"DELETE"})

print("С методом GET: ", response.text)
print("С методом POST: ", response1.text)
print("С методом PUT: ", response2.text)
print("С методом DELETE: ", response3.text)

# 4.2. POST
print("\n4.2. POST-запрос")
response = requests.post(url, data={"method":"GET"})
response1 = requests.post(url, data={"method":"POST"})
response2 = requests.post(url, data={"method":"PUT"})
response3 = requests.post(url, data={"method":"DELETE"})

print("С методом GET: ", response.text)
print("С методом POST: ", response1.text)
print("С методом PUT: ", response2.text)
print("С методом DELETE: ", response3.text)

# 4.3. PUT
print("\n4.3. PUT-запрос")
response = requests.put(url, data={"method":"GET"})
response1 = requests.put(url, data={"method":"POST"})
response2 = requests.put(url, data={"method":"PUT"})
response3 = requests.put(url, data={"method":"DELETE"})

print("С методом GET: ", response.text)
print("С методом POST: ", response1.text)
print("С методом PUT: ", response2.text)
print("С методом DELETE: ", response3.text)

# 4.4. DELETE
print("\n4.4. DELETE-запрос")
response = requests.delete(url, data={"method":"GET"})
response1 = requests.delete(url, data={"method":"POST"})
response2 = requests.delete(url, data={"method":"PUT"})
response3 = requests.delete(url, data={"method":"DELETE"})

print("С методом GET: ", response.text) # ошибка здесь. Сервер отвечает, что всё ок, при несовпадении методов.
print("С методом POST: ", response1.text)
print("С методом PUT: ", response2.text)
print("С методом DELETE: ", response3.text)