import telebot
import dotenv
import django
import os
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_server.settings")
django.setup()
from object_creator import create_user, create_message
#Получаем токен из окружения
dotenv.load_dotenv()
tg_token = os.environ['tgtoken']

#Инициализируем телеграм бота с помощью токена
diplom_bot = telebot.TeleBot(tg_token)

#Функция ждет сообщения из тг и обрабатывает их
@diplom_bot.message_handler(content_types=["text"])
def message_handler(message: callable) -> None:
    print("message in tg detected")
    user_id = message.from_user.id
    user_profile_photos = diplom_bot.get_user_profile_photos(user_id)
    if user_profile_photos.photos and user_profile_photos.photos[0]:
        first_photo = user_profile_photos.photos[0][0]
        file_id = first_photo.file_id
        file_path = diplom_bot.get_file(file_id).file_path
        picture_url = f'https://api.telegram.org/file/bot{diplom_bot.token}/{file_path}'
    else:
        picture_url = "http://localhost:8000/get_image/"
    print(picture_url)
    user_text = message.text.strip()
    user_name = message.from_user.first_name
    user = create_user(user_id, user_name, picture_url)
    create_message(user = user[0], sender = "user", text = user_text)


#В эту функцию нужно передать айди юзера телеграм и сообщение, оно отправится ему в телеграм
def send_message(id,answer):
    diplom_bot.send_message(id, answer)

#Код который запустится при старте программы
if __name__ == "__main__":
    try:
        print('bot polling started')
        diplom_bot.infinity_polling(skip_pending=True, none_stop=True)
    except Exception as e:
        print(f"An error occurred: {e}")