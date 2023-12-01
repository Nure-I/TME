from django.contrib import admin
from .models import  *
# Register your models here.

admin.site.register(Course)
admin.site.register(Resource)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(Project)