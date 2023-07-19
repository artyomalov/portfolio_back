from rest_framework.views import APIView
from .models import ServiceModel
from .serializers import ServiceModelSerializer
from rest_framework.response import Response
from rest_framework.request import Request
# from django.http import Http404


class GetServices(APIView):
    """
    List all services
    """

    def get(self, request: Request, format=None):
        services: list[ServiceModel] = ServiceModel.objects.all()
        serializer = ServiceModelSerializer(
            services,
            many=True,
        )
        return Response(serializer.data)


