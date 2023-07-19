from rest_framework.views import APIView
from .models import ProjectModel
from .serializers import ProjectModelSerializerPreview, \
    ProjectModelSerializerImages
from rest_framework.response import Response
from django.http import Http404
from rest_framework.request import Request
from const import BASE_URL


class GetProjects(APIView):
    """
    List all projects
    """

    def get(self, request: Request, format=None):
        projects: list[ProjectModel] = ProjectModel.objects.all()
        serializer = ProjectModelSerializerPreview(
            projects,
            many=True,
            context={'base_url': BASE_URL}
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

    def get(self, request: Request, pk: int, format=None):
        project = self.get_object(pk)
        serializer = ProjectModelSerializerImages(
            project,
            context={'base_url': BASE_URL}
        )
        return Response(serializer.data)
