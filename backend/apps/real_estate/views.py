from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Realestate
from .serializers import RealestateModelSerializer


class RealestateViewSet(viewsets.ModelViewSet):
    """
    A simple Viewset for viewing all categories
    """

    queryset = Realestate.objects.all()

    @extend_schema(responses=RealestateModelSerializer)
    def list(self, request):
        serializer = RealestateModelSerializer(self.queryset, many=True)
        return Response(serializer.data)
