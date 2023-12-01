from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Course(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length= 10000)
    rating = models.FloatField(default=0.0)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    #resources = models.ManyToManyField('Resource')
    reviews = models.ManyToManyField('Review', blank=True)
    tags = models.ManyToManyField('Tag')
    #instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    #start_date = models.DateField()
    #end_date = models.DateField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('video', 'Video'),
        ('article', 'Article'),
    ]

    name = models.CharField(max_length=255)
    content = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    url = models.URLField(blank=True)
    publication_date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='resource_files/', blank=True)
    views_count = models.IntegerField(default=0)
    downloads_count = models.IntegerField(default=0)
    # author = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    resources = models.ManyToManyField(Resource, related_name='topics')
    order = models.PositiveIntegerField(default = 0)
    descriptions = RichTextField(blank=True,null=True)
    # Other fields as needed

    def __str__(self):
        return self.course.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()


class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    def __str__(self):
        return self.first_name
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name