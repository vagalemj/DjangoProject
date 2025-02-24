from django.http import HttpResponse
from django.shortcuts import render
def say_hello(request):
    return HttpResponse("Hello from Django")

def greeting(request):
    return HttpResponse("Hello from Greet!!")

def home(request):
    return render(request, 'home.html')