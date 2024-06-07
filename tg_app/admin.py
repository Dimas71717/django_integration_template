from django.contrib import admin
from .models import user_model, message_model

# Register your models here.
admin.site.register(user_model)
admin.site.register(message_model)