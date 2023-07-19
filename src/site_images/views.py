from rest_framework.views import APIView
from .models import ImageModel
from .serializers import ImageModelSerializer
from rest_framework.response import Response
from django.http import Http404

class GetImages(APIView):
    '''
    List all images
    '''
    
    def get(self, requset, format=None):
        images = ImageModel.objects.all()
        serializer = ImageModelSerializer(images, many=True)
        return Response(serializer.data)


class GetImage(APIView):
    '''
    Returns one selected image
    '''
        
    def get_object(self, pk):
        try:
            return ImageModel.objects.get(pk=pk)
        except ImageModel.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageModelSerializer(image)
        return Response(serializer.data)