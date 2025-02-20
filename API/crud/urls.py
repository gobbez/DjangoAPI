from django.urls import path
from .views import ExampleView

urlpatterns = [
    path('exampleselect/', ExampleView.as_view(), name='select'),
    path('examplecreate/', ExampleView.as_view(), name='create'),
    path('exampleupdate/', ExampleView.as_view(), name='update'),
    path('exampledelete/', ExampleView.as_view(), name='delete'),
]