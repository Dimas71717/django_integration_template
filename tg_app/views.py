from django.shortcuts import render
from django.http import HttpResponse
from .models import user_model, message_model
from tg_bot import send_message
from django.http import JsonResponse
import os
from django.conf import settings
import datetime
def user_view(request):
    users = user_model.objects.all()
    messages = message_model.objects.all()
    return render(request, 'index.html', {'users': users, "messages": messages})



def create_message_from_site(request):
    print('starting message creating')
    current_time = str(datetime.datetime.now())
    text_message = request.POST.get('text_message')
    user_id = request.POST.get('user')
    print(f'Message text: {text_message}')
    print(f"User id: {user_id}")
    user_object = user_model.objects.get_or_create(user_id=user_id)
    message_model.objects.create(user=user_object[0], message_text=text_message, sender="bot", message_date = current_time)
    send_message(user_id, text_message)
    return JsonResponse({'status': 'success', 'user': user_id, 'text_message': text_message})

def get_image(request):
    image_path = os.path.join(settings.BASE_DIR, 'default_pic.jpg')
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/jpeg")