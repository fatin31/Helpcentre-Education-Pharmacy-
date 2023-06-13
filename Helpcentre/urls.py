from django.conf.urls import include, url
from django.contrib import admin

from django.urls import re_path,path
from first_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('first_app.urls')),
    path('', views.index),
    
]
