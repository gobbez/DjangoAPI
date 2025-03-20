from django.urls import path
from .views import PythonQuizAPI, UsersAPI

urlpatterns = [
    path('pythonquiz/', PythonQuizAPI.as_view(), name='pythonquiz'),
    path('users/', UsersAPI.as_view(), name='users'),
]
