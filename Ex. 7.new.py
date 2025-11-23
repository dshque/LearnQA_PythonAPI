import requests

print("4. GET, POST, PUT, DELETE с разными параметрами.")
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 4.1. GET
print("\n4.1. GET-запрос")
try:
    response = requests.get(url, params={"method":"GET"})
    print("С методом GET: ", response.text)
except:
    print("С методом GET: ОШИБКА")

try:
    response1 = requests.get(url, params={"method":"POST"})
    print("С методом POST: ", response1.text)
except:
    print("С методом POST: ОШИБКА")

try:
    response2 = requests.get(url, params={"method":"PUT"})
    print("С методом PUT: ", response2.text)
except:
    print("С методом PUT: ОШИБКА")

try:
    response3 = requests.get(url, params={"method":"DELETE"})
    print("С методом DELETE: ", response3.text)
except:
    print("С методом DELETE: ОШИБКА")

# 4.2. POST
print("\n4.2. POST-запрос")
try:
    response = requests.post(url, data={"method":"GET"})
    print("С методом GET: ", response.text)
except:
    print("С методом GET: ОШИБКА")

try:
    response1 = requests.post(url, data={"method":"POST"})
    print("С методом POST: ", response1.text)
except:
    print("С методом POST: ОШИБКА")

try:
    response2 = requests.post(url, data={"method":"PUT"})
    print("С методом PUT: ", response2.text)
except:
    print("С методом PUT: ОШИБКА")

try:
    response3 = requests.post(url, data={"method":"DELETE"})
    print("С методом DELETE: ", response3.text)
except:
    print("С методом DELETE: ОШИБКА")

# 4.3. PUT
print("\n4.3. PUT-запрос")
try:
    response = requests.put(url, data={"method":"GET"})
    print("С методом GET: ", response.text)
except:
    print("С методом GET: ОШИБКА")

try:
    response1 = requests.put(url, data={"method":"POST"})
    print("С методом POST: ", response1.text)
except:
    print("С методом POST: ОШИБКА")

try:
    response2 = requests.put(url, data={"method":"PUT"})
    print("С методом PUT: ", response2.text)
except:
    print("С методом PUT: ОШИБКА")

try:
    response3 = requests.put(url, data={"method":"DELETE"})
    print("С методом DELETE: ", response3.text)
except:
    print("С методом DELETE: ОШИБКА")

# 4.4. DELETE
print("\n4.4. DELETE-запрос")
try:
    response = requests.delete(url, data={"method":"GET"})
    print("С методом GET: ", response.text)
except:
    print("С методом GET: ОШИБКА")

try:
    response1 = requests.delete(url, data={"method":"POST"})
    print("С методом POST: ", response1.text)
except:
    print("С методом POST: ОШИБКА")

try:
    response2 = requests.delete(url, data={"method":"PUT"})
    print("С методом PUT: ", response2.text)
except:
    print("С методом PUT: ОШИБКА")

try:
    response3 = requests.delete(url, data={"method":"DELETE"})
    print("С методом DELETE: ", response3.text)
except:
    print("С методом DELETE: ОШИБКА")
