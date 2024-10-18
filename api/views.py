from rest_framework import viewsets,status
from .models import Problem
from .serializers import ProblemSerializer
from .scraper import return_data_dict  # Import your scraper function
from rest_framework.decorators import action
from rest_framework.response import Response

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    @action(detail=False, methods=['get'], url_path='by-number/(?P<number>[^/.]+)')
    def get_by_number(self, request, number=None):
        try:
            # Filter the problem by its number
            number = str(number).zfill(4)
            problem = Problem.objects.get(number=number)
            serializer = self.get_serializer(problem)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Problem.DoesNotExist:
            return Response(
                {"detail": "Problem not found."},
                status=status.HTTP_404_NOT_FOUND
            )
    # Custom action to get a problem by URL name
    @action(detail=False, methods=['get'], url_path='by-name/(?P<url_name>.+)')
    def get_by_url_name(self, request, url_name=None):
        # Find the problem by checking if the given URL name is in the link field
        try:
            problem = Problem.objects.get(link__icontains=url_name)
            serializer = self.get_serializer(problem)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Problem.DoesNotExist:
            return Response(
                {"error": "Problem not found with the given URL name"},
                status=status.HTTP_404_NOT_FOUND
            )