from django.shortcuts import render
from django.http import HttpResponse
from Foodapp.models import Item

# Create your views here.
def home(request):
    li = Item.objects.all()
    context = {
        'li': li,
    }
    return render(request, 'home.html', context)