from django.urls import path
from .views import PythonQuizView

urlpatterns = [
    path('getpythonquiz/', PythonQuizView.as_view(), name='getquiz'),
    path('addpythonquiz/', PythonQuizView.as_view(), name='addquiz'),
]