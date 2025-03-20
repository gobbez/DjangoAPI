from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import PythonQuiz, Users
from .serializers import PythonQuizSerializer, UsersSerializer

class PythonQuizAPI(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve all quiz questions",
        responses={200: PythonQuizSerializer(many=True)}
    )
    def get(self, request):
        quizzes = PythonQuiz.objects.all()
        serializer = PythonQuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new quiz question",
        request_body=PythonQuizSerializer,
        responses={201: "Created", 400: "Bad Request"}
    )
    def post(self, request):
        serializer = PythonQuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersAPI(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve all users and their quiz performance",
        responses={200: UsersSerializer(many=True)}
    )
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
