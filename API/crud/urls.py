from django.urls import path
from .views import ExampleListCreateView, ExampleDetailView

urlpatterns = [
    path('example/', ExampleListCreateView.as_view(), name='example-list'),
    path('example/<int:id>/', ExampleDetailView.as_view(), name='example-detail'),
]
