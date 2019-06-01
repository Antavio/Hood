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

    def test_delete_instance(self):
        self.new_hood.delete_hood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)==0)

    def test_find_hood(self):
        self.new_hood.save_hood()
        neighbourhood = Neighborhood.search_neighbourhood(1)
        self.assertEqual(neighbourhood.hood_name,'Mtaani')

    def test_update_hood(self):
        self.new_hood.save_hood()
        neighborhood = Neighborhood.search_neighbourhood(1)
        neighborhood.hood_name = 'Updated Mtaa'
        self.assertEqual(neighborhood.hood_name,'Updated Mtaa')

class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_hood = Neighborhood(id=1,hood_name='Mtaani',hood_location="Nairobi",occupants=10)
        self.new_hood.save_hood()
        self.new_biz = Business(id=1,business_name='Bizna',business_email="biz@mail.com",business_owner=self.new_user,business_hood_id=self.new_hood)            

    def test_instance(self):
        self.assertTrue(isinstance(self.new_biz,Business))

    def test_save_instance(self):
        self.new_biz.save_business()
        biznas = Business.objects.all()
        self.assertTrue(len(biznas)>0)

    def test_delete_instance(self):
        self.new_biz.delete_business()
        biznas = Business.objects.all()
        self.assertTrue(len(biznas)==0)

    def test_find_biz(self):
        self.new_biz.save_business()
        bizz = Business.search_business(1)
        self.assertEqual(bizz.business_name,'Bizna')

    def test_update_business(self):
        self.new_biz.save_business()
        bizz = Business.search_business(1)
        bizz.business_name = 'Updated Bizna'
        self.assertEqual(bizz.business_name,'Updated Bizna')


class PostTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_hood = Neighborhood(id=1,hood_name='Mtaani',hood_location="Nairobi",occupants=10)
        self.new_hood.save_hood()
        self.new_post = Post(id=1,post_name="Posting",post_description='Post Description',date_posted='2018-05-04',post_owner=self.new_user,hood_post=self.new_hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_instance(self):
        self.new_post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)

    def test_delete_instance(self):
        self.new_post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post)==0)

class ContactTestClass(TestCase):
    def setUp(self):
        self.new_hood = Neighborhood(id=1,hood_name='Mtaani',hood_location="Nairobi",occupants=10)
        self.new_hood.save_hood()
        self.new_contact = ContactInfo(id=1,health_department='Health',police_department='Police',hood=self.new_hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_contact,ContactInfo))

    def test_save_instance(self):
        self.new_contact.save_contact()
        contact = ContactInfo.objects.all()
        self.assertTrue(len(contact)>0)

    def test_delete_instance(self):
        self.new_contact.delete_contact()
        contact = ContactInfo.objects.all()
        self.assertTrue(len(contact)==0)