from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_photo/', add_photo, name='add_photo'),
    path('card_view/<str:pk>/', card_view, name='card_view'),
]