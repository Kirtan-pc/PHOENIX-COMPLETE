from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('chat/', views.chat_page, name='chat'),
    path('api/chat/', views.api_chat, name='api_chat'),
]
