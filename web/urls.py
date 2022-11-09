from django.urls import path, include
from web.views import *
from unicodedata import name

app_name='web'

urlpatterns = [
    
    path('', Index, name='home'),
    

]