from app2.views import app2_function
from typing import Pattern
from django.conf.urls import url
from django.urls import path
from app2.views import *

app_name="app2_function"
urlpatterns = [
    path("app2_function/",app2_function,name="app2_function"),
]