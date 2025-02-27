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

def details(request, item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item': item
    }
    return render(request, 'details.html', context)