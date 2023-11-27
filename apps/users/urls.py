from django.urls import path
from .views import *

urlpatterns = [
    path('', user_main, name='user_main'),
]
