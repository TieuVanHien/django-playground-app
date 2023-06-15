from django.urls import path
from . import views

#url config
urlpatterns = [
    path('', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
]
