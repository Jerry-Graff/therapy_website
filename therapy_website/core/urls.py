from django.urls import path
from . import views


urls_patterns = [
    path("", views.home, name="home"),
    path("send/", views.form_send, name="form_send"),
]
