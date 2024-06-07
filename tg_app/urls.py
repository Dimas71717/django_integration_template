from django.urls import path
from . import views
from .views import create_message_from_site
urlpatterns = [
    path('', views.user_view),
    path('create_message_from_site/', create_message_from_site, name='create_message_from_site'),
    path('get_image/', views.get_image, name='get_image')
]
