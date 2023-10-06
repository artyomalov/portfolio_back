from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import ContactModel
from .serializers import ContactModelSerializer


class GetContacts(APIView):
    """
    List all contacts' data
    """

    def get(self, request: Request, format=None):
        contacts: list[ContactModel] = ContactModel.objects.all()
        serializer = ContactModelSerializer(contacts, many=True)

        return Response(serializer.data)
