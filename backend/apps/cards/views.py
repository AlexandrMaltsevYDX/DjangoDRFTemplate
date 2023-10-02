from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, parsers
from rest_framework.response import Response

from .models import CardModel
from .serializers import CardModelSerializer


class CardModelViewSet(viewsets.ModelViewSet):
    """
    A simple Viewset for viewing all cards
    """

    queryset = CardModel.objects.all()
    serializer_class = CardModelSerializer
    parser_classes = (parsers.MultiPartParser,)

    @extend_schema(description="Custom description for the endpoint")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        request=CardModelSerializer,
        responses={200: CardModelSerializer()},
        methods=["POST"],
        summary="Upload a file",
        description="Upload a file for YourModel.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
