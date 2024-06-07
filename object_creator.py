import dotenv
dotenv.load_dotenv()
import django
django.setup()
from tg_app.models import user_model, message_model
import datetime

def create_user(user_id, user_name, picture_url):
    user = user_model.objects.get_or_create(user_id = user_id, user_name = user_name, picture_url = picture_url)
    return user

def create_message(user, sender, text):
    current_time = str(datetime.datetime.now())
    user_message = message_model.objects.create(message_date = current_time, message_text = text, user = user, sender = sender)
    return user_message
