from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="index"),
    path('about/', about,name="about"),
    path('create/', create,name="create"),
    path('delete/<int:id>', delete, name="delete"),
    path('yes_finish/<int:id>', yes_finish, name="yes_finish"),
    path('no_finish/<int:id>', no_finish, name="no_finish"),
    path('update/<int:id>', update, name="update"),
]