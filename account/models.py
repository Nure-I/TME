from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
  EDU_LEVEL = [
        ('Elementary', 'Elementary'),
        ('Highschool', 'Highschool'),
        ('Gradudate', 'Gradudate'),
        ('Masters', 'Masters'),
    ]
  user= models.OneToOneField(User, null=True , on_delete= models.CASCADE )
  proffession = models.CharField(max_length=50)
  edu_level = models.CharField(max_length=20, choices=EDU_LEVEL)
  
  def __str__(self):
      return self.user.first_name