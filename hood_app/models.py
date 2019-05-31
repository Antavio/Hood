from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=0)

    def __str__(self):
        return self.hood_name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    user_location = models.CharField(max_length=200)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    hood_id = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Business(models.Model):
    business_name = models.CharField(max_length=200)
    business_email = models.EmailField()
    business_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    business_hood_id = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['-id']

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    @classmethod
    def search_project_by_title(cls,search_term):
        post = cls.objects.filter(post_name__icontains=search_term)
        return post    
    
    

class Post(models.Model):
    post_picture = models.ImageField(upload_to='posts/',blank=True)
    post_name = models.CharField(max_length=200)
    post_description = models.TextField()
    date_posted = models.DateField(auto_now=True)

    def __str__(self):
        return self.post_name

class ContactInfo(models.Model):

    health_department = models.CharField(max_length=200)
    police_department = models.CharField(max_length=200)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.health_department

