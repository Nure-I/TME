from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   # path('create_user', views.create_user, name='create_user'),
   # path('directors', views.directors, name='directors'),
    path('createCourse', views.createCourse, name='createCourse'),
    path('courseList', views.courseList, name='courseList'),
    path('courseDetail/<int:courseId>/', views.courseDetail, name='courseDetail'),
    path('removeCourse/<int:courseId>/', views.removeCourse, name='removeCourse'),
    path('createSubTopic/<int:courseId>/', views.createSubTopic, name='createSubTopic'),
    path('createResource', views.createResource, name='createResource'),
    path('resourceList', views.resourceList, name='resourceList'),
    path('resourceDetail/<int:resourceId>/', views.resourceDetail, name='resourceDetail'),
    path('removeResource/<int:resourceId>/', views.removeResource, name='removeResource'),


    path('subTopicDetail/<int:subTopicId>/', views.subTopicDetail, name='subTopicDetail'),
    path('removeSubTopic/<int:subTopicId>/', views.removeSubTopic, name='removeSubTopic'),
   # path('confirm/<int:request_id>/', views.confirm_requests, name='confirm_requests'),
   # path('approve/<int:request_id>/', views.approve_requests, name='approve_requests'),
]