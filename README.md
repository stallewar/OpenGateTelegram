# OpenGate Telegram Script

## Описание
Телеграм клиент с использованием библиотеки Telethon.

## Для чего
Для отравки запроса боту для отрытия шлагбаума. В Android Telegram нельзя создать свой ярлык для отправки готового сообщения, этот скрипт используется совместно с Termux Widget.

## Требования
- Python 3.x
- Библиотека Telethon
- Учетная запись Telegram с доступом к API
- API ID и Hash вашего Telegram аккаунта (my.telegram.org)
- Номер телефона и пароль вашего Telegram аккаунта
- Username или chat_id бота, которому будет отправлено сообщение
- Termux
- Termux Widget

## Установка
1. Установите Python 3.x на телефон в termux, выполнить `pkg install python`.
2. Установите библиотеку Telethon с помощью pip: `pip install telethon`.
3. В файле `openGate.py` замените `YOUR_TG_PHONE_NUMBER`, `YOUR_TG_PASSWORD`, `API_HASH`, `API_NAME` и `BOT_NAME` своими значениями. Укажите нужную вам команду в `message_text`.
4. Установите Termux Widget и следуйте инструкции: [https://github.com/termux/termux-widget](https://github.com/termux/termux-widget).

## Первый запуск
Запустите скрипт в termux с помощью команды `python openGate.py` или через bash script `openGate.sh`. Введите полученный от телеграм код сессии. Должен появиться файл - `openGateSession`, после этого скрипт будет работать при активации ярлыка termux-widget.

## Обработка ошибок
Скрипт обрабатывает следующие ошибки:
- **SessionPasswordNeededError**: Ошибка, возникающая при необходимости ввода пароля сеанса.
- **PhoneNumberBannedError**: Ошибка, возникающая при заблокированном номере телефона.
- **PhoneNumberFloodError**: Ошибка, возникающая при превышении лимита отправки сообщений.
- **PhoneMigrateError**: Ошибка, возникающая при изменении номера телефона.
- **ConnectionError**: Ошибка, возникающая при проблемах с подключением к Telegram API.
- **Exception**: Общая ошибка, возникающая при любых других проблемах.

## Закрытие сеанса
Скрипт закрывает сеанс клиента после отправки сообщения.
