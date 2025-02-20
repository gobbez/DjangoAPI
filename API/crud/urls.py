from django.urls import path
from .views import ExampleView

urlpatterns = [
    path('exampleselect/', ExampleView.as_view(), name='selectall'),
    path('exampleselect/<int:input_id>/', ExampleView.as_view(), name='selectone'),
    path('examplecreate/', ExampleView.as_view(), name='create')
]