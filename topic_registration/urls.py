from django.urls import path
from . import views

app_name = 'topic_registration'
urlpatterns = [
    path('', views.topic_registration, name='topic_registration'),
    path('register', views.topic_register, name='topic_register')
]
