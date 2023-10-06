from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import Http404
from django.conf import settings
from .models import ProjectModel
from .serializers import ProjectModelSerializerPreview, \
    ProjectModelSerializerImages


class GetProjects(APIView):
    """
    List all projects
    """

    def get(self, request: Request, format=None):
        projects: list[ProjectModel] = ProjectModel.objects.all()
        serializer = ProjectModelSerializerPreview(
            projects,
            many=True,
            context={'base_url': settings.BASE_URL}
        )
        return Response(serializer.data)


class GetProject(APIView):
    """
    Returns one project
    """

    def get_object(self, pk):
        try:
            return ProjectModel.objects.get(pk=pk)
        except ProjectModel.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: str, format=None):
        pk_to_number = int(pk)
        project = self.get_object(pk_to_number)
        serializer = ProjectModelSerializerImages(
            project,
            context={'base_url': settings.BASE_URL}
        )
        return Response(serializer.data)
