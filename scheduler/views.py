# scheduler/views.py
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Task

def homepage(request):
    # Retrieve all events from the database
    return render(request, 'homepage.html')

def selecttasks(request):
    return render(request, "selecttasks.html")

def schedule(request):
    return render(request, "schedule.html")

def chatbot(request):
    return render(request, 'chatbot.html')

