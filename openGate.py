import logging

import telethon
from telethon.errors import (
    ConnectionSystemEmptyError,
    PhoneMigrateError,
    PhoneNumberBannedError,
    PhoneNumberFloodError,
    SessionPasswordNeededError,
)
from telethon.sync import TelegramClient
from telethon.tl.types import Message

# Укажите номер телефона и API ID/Hash вашего Telegram аккаунта
MSISDN = "YOUR_TG_PHONE_NUMBER"
TG_PASSWORD = "YOUR_TG_PASSWORD"
SESSION = "OpenGateSession"
# Используйте свои значения из my.telegram.org
API_ID = 123456
API_HASH = "API_HASH"
# Укажите username или chat_id бота(адресата)
BOT_USERNAME = "@BOT_NAME"
# Текст сообщения для бота
MESSAGE_TEXT = "/open1"

# Настройте логирование
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Объект клиента Telegram
client = TelegramClient(SESSION, API_ID, API_HASH)

# Регистрируем клиента (в первый раз нужно будет ввести код из SMS)
client.start(phone=MSISDN, password=TG_PASSWORD)


# Отправим сообщение боту
logging.info(f"Sending message '{MESSAGE_TEXT}' to {BOT_USERNAME}")
sent_message: Message = client.send_message(BOT_USERNAME, MESSAGE_TEXT)
message_status = sent_message.message
logging.info(f"Message status: {message_status}")

try:
    pass
except SessionPasswordNeededError:
    logging.error("Session password is needed")
    # Handle the SessionPasswordNeededError here

except PhoneNumberBannedError as e:
    logging.error("Phone number is banned")
    # Handle the PhoneNumberBannedError here

except PhoneNumberFloodError:
    logging.error("Phone number is flooded")
    # Handle the PhoneNumberFloodError here

except PhoneMigrateError:
    logging.error("Phone number has been migrated")
    # Handle the PhoneMigratedError here

except ConnectionError as e:
    logging.error(f"Connection error occurred: {str(e)}")
    # Handle the ConnectionError here

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    # Handle other exceptions here

finally:

    # Закрыываем сеанс клиента
    logging.info("Closing client session")
client.disconnect()
