from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(id=1,prof_user=self.new_user,user_location='Turkana')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.new_hood = Neighborhood(id=1,hood_name='Mtaani',hood_location="Nairobi",occupants=10)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,Neighborhood))

    def test_save_instance(self):
        self.new_hood.save_hood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_find_hood(self):
        self.new_hood.save_hood()
        neighbourhood = Neighborhood.search_neighbourhood(1)
        self.assertEqual(neighbourhood.hood_name,'Mtaani')

    def test_update_hood(self):
        self.new_hood.save_hood()
        neighborhood = Neighborhood.search_neighbourhood(1)
        neighborhood.hood_name = 'Updated Mtaa'
        self.assertEqual(neighborhood.hood_name,'Updated Mtaa')