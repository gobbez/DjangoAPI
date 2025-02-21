from django.db import models


class PythonQuiz(models.Model):
    """Create the table for quiz"""
    question = models.CharField(max_length=255)
    A = models.CharField(max_length=255)
    B = models.CharField(max_length=255)
    C = models.CharField(max_length=255)
    D = models.CharField(max_length=255)
    correct = models.CharField(max_length=255)
    points = models.IntegerField()


class Users(models.Model):
    """Create table users to log correct or wrong answers"""
    username = models.CharField(max_length=255)
    right = models.IntegerField()
    wrong = models.IntegerField()
