from django.shortcuts import render
from rest_framework import viewsets
from main import models, serializers

# Create your views here.


class BookViewsets(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
