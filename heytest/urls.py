from django.contrib import admin
from django.urls import path
from django.conf.urls import re_path

# local imports
from heytest.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^prueba/answer', views.getAnswer),
    re_path(r'^prueba/domingos', views.getDomingos),
    re_path(r'^prueba/password', views.getPassword),
    re_path(r'^prueba/fibopan', views.getFibopan),
    re_path(r'^prueba/pascals', views.getPascals),
]
