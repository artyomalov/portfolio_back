from django.urls import path
from .views import GetContacts

urlpatterns = [
    path('contacts/', GetContacts.as_view(), name='all_contacts'),
]
