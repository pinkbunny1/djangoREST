from rest_framework import serializers # Imports serializers class from rest_framework module
from .models import Bucketlist # Imports Bucketlist Model class from model.py


class BucketlistSerializer(serializers.ModelSerializer):
    """
        Serializer to map the Model instance into JSON format.
        (Serialises Model Instance --> JSON)
    """

    class Meta:
        """
            Meta class maps serialiser's fields with model fields.
            (Serialisers fields --> Model fields)
        """
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
