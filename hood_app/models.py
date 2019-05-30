from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=100)
    hood_location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=0)

    def __str__(self):
        return self.hood_name

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    user_location = models.CharField(max_length=200)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    hood_id = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

class Business(models.Model):
    business_name = models.CharField(max_length=200)
    business_email = models.EmailField()
    business_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    business_hood_id = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['-id']