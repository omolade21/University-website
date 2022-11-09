
from django.contrib import admin
from django.urls import re_path, path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import *
from web.views import *
from django.contrib.auth import views as auth_views


admin.site.site_header = "PelicanEstate Admin"
admin.site.site_title = "PelicanEstate Admin Portal"
admin.site.index_title = "Welcome to PelicanEstate Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', admin.site.urls),
    path('', include('web.urls', namespace='web')),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('api.urls', namespace='api')),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)

