from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

"""
 BucketlistSerializer:
     model = Bucketlist
     fields = ('id', 'name', 'date_created', 'date_modified')
     read_only_fields = ('date_created', 'date_modified')

"""
class CreateView(generics.ListCreateAPIView):
    """
        - Deinfes the create behaviour(POST) of the rest api
        - Handles "reverse('create')"
        - The 'ListCreateAPIView' is a generic view which provides GET (list all) and POST method handlers
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save post data when creating a new bucketlist."""
        serializer.save()





class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
        - Handles http GET, PUT, DELETE requests
        - reverse('details') in test.py
        - RetrieveUpdateDestroyAPIView is a generic view that provides GET(one), PUT, PATCH and DELETE method handlers.
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
