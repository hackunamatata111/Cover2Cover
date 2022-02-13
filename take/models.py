from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Take(models.Model):
    roll=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    auth=models.CharField(max_length=200,null=True, blank=True)
    contact=models.CharField(max_length=200,null=True, blank=True) #email
    mob=models.IntegerField(null=True, blank=True)
    time=models.DateTimeField(auto_now_add=True)
    course=models.CharField(max_length=200, null=True)
    cname=models.CharField(max_length=100, null=True)

    class Meta:
        ordering=['name']
    def __str__(self):
        return self.name    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    name=models.CharField(max_length=100, null=True)
    mob=models.IntegerField(null=True)
    cname=models.CharField(max_length=100, null=True)
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



