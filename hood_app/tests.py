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
