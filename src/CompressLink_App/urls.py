from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path("", index, name='index'),
    
    re_path(r"^(?P<code>[a-zA-Z0-9]{6})$", redirection, name='redirect'),

    path('createlink', createlink, name='createlink')
]