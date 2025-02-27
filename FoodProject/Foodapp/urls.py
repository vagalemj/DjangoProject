from django.urls import path, include
from . import views

app_name = 'Foodapp'
urlpatterns = [
    path('home/', views.home),
    path('<int:item_id>/', views.details, name = 'details'),
]