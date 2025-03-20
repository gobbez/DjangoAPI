from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Example
from .serializers import ExampleSerializer

class ExampleListCreateView(ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    @swagger_auto_schema(
        operation_description="Retrieve all records",
        responses={200: ExampleSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new record",
        request_body=ExampleSerializer,
        responses={201: ExampleSerializer()}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ExampleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    lookup_field = 'id'  # Permette di cercare per ID

    @swagger_auto_schema(
        operation_description="Retrieve a single record",
        responses={200: ExampleSerializer(), 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a record",
        request_body=ExampleSerializer,
        responses={200: ExampleSerializer(), 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a record",
        responses={204: "Deleted", 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
