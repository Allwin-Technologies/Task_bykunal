from django.db import models
from django.contrib.auth.models import User

# Create your models here.
user_choice = ([('private','private'),('public','public'),('Other','Other')])
class Person(models.Model):
    user_id = models.IntegerField()
    user_type  = models.CharField(max_length=20,choices = user_choice)
    timestamp = models.DateTimeField()
    
    def __str__(self) :
        return self.user_type

class Image(models.Model):
    user_id = models.ForeignKey(Person)
    person_image = models.ImageField(upload_to='person_img',null=True,blank=True)