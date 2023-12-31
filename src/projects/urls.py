from django.urls import path
from .views import GetProjects, GetProject

urlpatterns = [
    path('projects/', GetProjects.as_view(), name='all_images'),
    path('project/<str:pk>/', GetProject.as_view(), name='projects'),
]


