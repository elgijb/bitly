# Сокращатель ссылок Bitly

Этот скрипт на Python взаимодействует с API Bitly для выполнения функций сокращения URL и отслеживания кликов. Он предоставляет следующие возможности:

- Сокращение URL: По заданному длинному URL скрипт использует API Bitly для создания сокращенной ссылки (Bitlink).
- Отслеживание кликов: Если вводится Bitlink, скрипт извлекает и отображает общее количество кликов по этой ссылке.
- Проверка является ли URL Bitlink: Скрипт определяет, является ли заданный URL уже Bitlink'ом.

## Предварительные требования

Перед запуском этого скрипта убедитесь, что у вас есть следующие компоненты:

- Установленный Python на вашем компьютере (рекомендуется версия 3.x).
- Установленная библиотека requests (`pip install requests`).
- Установленная библиотека python-dotenv (`pip install python-dotenv`).

## Установка

1. Склонируйте этот репозиторий на свой компьютер:

     git clone https://github.com/your_username/bitly-link-shortener.git
   
2. Перейдите в директорию проекта:

     cd bitly-link-shortener
   
3. Создайте виртуальное окружение (необязательно, но рекомендуется):

     python -m venv venv
   source venv/bin/activate  # Активируйте виртуальное окружение (для Unix/Mac)
   
4. Установите необходимые зависимости:

     pip install -r requirements.txt
   
5. Получите токен доступа Bitly (Bitly Access Token):

   - Зарегистрируйтесь или войдите в [Bitly](https://bitly.com/)
   - Перейдите в [Консоль разработчика Bitly](https://dev.bitly.com/)
   - Создайте общий (Generic) токен доступа (если у вас его еще нет)

6. Создайте файл .env в корневой директории проекта и добавьте в него ваш токен доступа Bitly:

     BITLY_TOKEN=ваш_токен_доступа_сюда
   
## Использование

Запустите скрипт из командной строки:
python bitly_link_shortener.py

Следуйте инструкциям в консоли:

- Введите URL для сокращения или отслеживания кликов.
- Скрипт определит, является ли введенный URL Bitlink'ом или обычным URL и выполнит соответствующее действие.

## Пример
$ python bitly_link_shortener.py
Введите ссылку для сокращения:https://example.com
ссылка: https://bit.ly/abcdef

$ python bitly_link_shortener.py
Введите ссылку для сокращения:https://bit.ly/abcdef
Количество кликов: 100

## Примечания

- Скрипт использует библиотеку requests для отправки HTTP-запросов к API Bitly.
- Реализовано обработка ошибок для управления исключениями, которые могут возникнуть во время запросов к API.
- Обязательно храните свой токен доступа Bitly в безопасности и не делитесь им публично.

Наслаждайтесь сокращением и отслеживанием ваших URL с Bitly!