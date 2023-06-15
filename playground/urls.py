from django.urls import path
from . import views

#url config
urlpatterns = [
    path('', views.say_hello),
]
