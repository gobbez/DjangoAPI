from rest_framework import serializers
from .models import PythonQuiz, Users

class PythonQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuiz
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
