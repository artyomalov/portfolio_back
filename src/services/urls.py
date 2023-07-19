from django.urls import path
from .views import GetServices

urlpatterns = [
    path('services/', GetServices.as_view(), name='all_services')
]