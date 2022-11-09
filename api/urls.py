from django.urls import path, include
from web.views import *
from unicodedata import name

app_name='api'

urlpatterns = [
    
    path('', Index, name='home'),
    

]