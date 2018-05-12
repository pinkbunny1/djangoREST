from django.db import models

# Create your models here.
"""
    After making changes to models.py file --> Migrate !
    --> python3 manage.py makemigrations [Creates a new migration based on models.py]
    --> python3 manage.py migrate [Apply the new migration to the database]
    
    Migrations are Django’s way of propagating changes you make to the models(models.py) (like adding a field, deleting a model, etc.) into the database schema.
"""

class Bucketlist(models.Model):
    """
    - Define fields that will represent the table fields in the database.
    - Represents the Bucketlist Model.
    """
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns human readable representation of model instance.
        """
        return "{}".format(self.name)
