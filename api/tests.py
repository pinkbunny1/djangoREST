from django.test import TestCase

# Create your tests here.
from .models import Bucketlist

# View test
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


""" this file: imports TestCase from django.test. TestCase object has a single test which tests whether the model can create a Bucketlist with a name."""

""" To Test --> python3 manage.py test """



class ModelTestCase(TestCase):
    """This class defines the test suite(a set of test programs) for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name = "bucketlist name given by user/test"
        self.bucketlist = Bucketlist(name=self.bucketlist_name) # Creates a Bucketlist model with the given NAME

    def test_model_can_create_a_bucketlist(self):
        """Test if the bucketlist model can create a bucketlist with the given bucketlist_name."""
        old_count = Bucketlist.objects.count()#Count how many data objs in the beginning
        self.bucketlist.save()#save the new data obj
        new_count = Bucketlist.objects.count()#Count how many data objs after saving
        self.assertNotEqual(old_count, new_count) # see if old_count and new_count NOT EQUAL. if so, test is passed.


"""
    reverse('name'): name is defined in api/urls.py
"""

class ViewTestCase(TestCase):
    """
        Test programe for the api app views.
    """

    def setUp(self):
        """
            Define the test client and other test variables.
        """
        self.client = APIClient()
        self.bucketlist_data = {'name' : 'Go to Italy'}
        self.response = self.client.post(
                            reverse('create'),
                            self.bucketlist_data,
                            format="json")


    def test_api_can_create_a_bucketlist(self):
        """
            Test if api has bucket creation ability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED) #See if response status code is EQUAL to 201. if so, Test is passed.

    def test_api_can_get_a_bucketlist(self):
        """
            Test if the api can get/fetch a chosen bucketlist
        """
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
                        reverse('details', kwargs={'pk': bucketlist.id}),
                        format="json")
                        # pk : unique ID key in database
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """
            Test if api can update a chosen bucketlist by user
        """
        change_bucketlist = {'name': 'Something New'}
        bucketlist = Bucketlist.objects.get()
        res = self.client.put(
                reverse('details', kwargs={'pk':bucketlist.id}),
                change_bucketlist,
                format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """
            Test if api can delete a chosen bucketlist
        """
        bucketlist = Bucketlist.objects.get()
        res = self.client.delete(
                reverse('details', kwargs={'pk': bucketlist.id}),
                format="json",
                follow=True
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
