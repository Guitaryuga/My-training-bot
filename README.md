# MyTrainingBot

MyTrainingBot -  чат-бот для Telegram, на котором я отрабатываю код и те или иные фичи

На данный момент бот умеет:
- Приветствовать пользователя и вести лог своих действий
- Сообщать, в каком созвездии в данный момент находится та или иная планета солнечной системы(на английском языке)
- Сообщать дату следующего полнолуния
- Рикроллить пользователя(Never gonna give you up...)
- Считать в слова в сообщении пользователя
- Играть в игру с загадыванием чисел
- Присылать картинки с сиба-ину
- Умеет присваивать смайлик пользователю на время общения, может определять геолокацию и имеет простую клавиатуру для некоторых действий

### Установка

1. Клонируйте репозиторий, создайте виртуальное окружение, в зависимости от вашей ОС
2. Установите зависимости `pip install -r requirements.txt`
3. Создайте файл settings.py и создайте в нем переменные:
    ```
    API_KEY = "Ключ вашего бота"
    PROXY_URL = "URL socks5-прокси"
    PROXY_USERNAME = "Username для авторизации на прокси"
    PROXY_PASSWORD = "Пароль  для авторизации на прокси"
    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
