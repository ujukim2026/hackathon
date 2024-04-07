# scheduler/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('selecttasks/', views.selecttasks, name='selecttasks'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('schedule/', views.schedule, name='schedule'),
] 
