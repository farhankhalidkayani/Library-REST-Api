from django.shortcuts import render
from rest_framework import viewsets, filters
from main import models, serializers

# Create your views here.


class BookViewsets(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author", "genre"]
