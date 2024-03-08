# DRF
from rest_framework import viewsets
from rest_framework.response import Response
# Serializer
from .serializers import BooksSerializer
# Models
from ..models import Books


class BooksViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(data=serializer.data)