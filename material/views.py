from django.urls import reverse
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .forms import CourseForm , EditCourseForm, SubTopicForm, ResourceForm, EditResourceForm, EditSubTopicForm
from .models import Course, Topic , Resource
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='logIn')
def createCourse(request):
  form = CourseForm()
  if request.method == 'POST':
      form = CourseForm(request.POST)
      if form.is_valid():
          name = form.cleaned_data.get('name')
          difficulty_level = form.cleaned_data.get('difficulty_level')
          courseExist = Course.objects.filter(name= name, difficulty_level= difficulty_level)
          if courseExist:
            messages.success(request, f'Sorry, {name} course is Already in the list!')
            return redirect('courseList')
          else:
            form.save()
            course = Course.objects.get(name= name, difficulty_level= difficulty_level)
            messages.success(request, f'You have successfully created {name} course.')
            redirect_url = reverse('courseDetail', kwargs={'courseId': course.id})
            return redirect(redirect_url)
            # return redirect('createSubTopic')
      else:
          for field, errors in form.errors.items():
              for error in errors:
                  messages.warning(request, f'{error}')
  return render(request,'material/add_course.html',{'form':form})


@login_required(login_url='logIn')
def courseList(request):
  # courses = Course.objects.prefetch_related('resources').all()
  courses = Course.objects.all()
  return render(request, 'material/course_list.html', {'courses': courses})


@login_required(login_url='logIn')
def courseDetail(request,courseId):
 # course = Course.objects.prefetch_related('resources').get(id= courseId)
  course = Course.objects.get(id= courseId)
  subTopics = Topic.objects.filter(course=course) 
  if request.method == 'POST':
    form_identifier = request.POST.get('form_identifier')
    if form_identifier == 'courseForm':
      form = EditCourseForm(request.POST, instance=course)
      if form.is_valid():
          form.save()
          name = form.cleaned_data.get('name')
          messages.success(request, f'You have successfully Updated {name} course.')
          return redirect('courseList')
      else:
          for field, errors in form.errors.items():
              for error in errors:
                  messages.warning(request, f'{error}')
    elif form_identifier == 'subtopicForm':
      form = SubTopicForm(request.POST, instance=course)
  else:
    form = EditCourseForm(instance= course)
    sform = SubTopicForm()
    rform = ResourceForm()
  context = {'form':form,'sform':sform,'rform':rform,'course':course,'subTopics':subTopics} 
  return render(request,'material/course_detail.html',context)


@login_required(login_url='logIn')
def removeCourse(request,courseId):
  course = Course.objects.get(id = courseId)
  course.delete()
  messages.success(request, f'You have successfully Removed {course.name} course.')
  return redirect('courseList')
 

@login_required(login_url='logIn')
def createSubTopic(request,courseId):
  course = Course.objects.get(id=courseId)
  form = SubTopicForm()
  if request.method == 'POST':
      form = SubTopicForm(request.POST)
      if form.is_valid():
          name = form.cleaned_data.get('name')
          order = form.cleaned_data.get('order')
          topic = Topic.objects.filter(name= name, order= order)
          if topic:
            messages.success(request, f'Sorry, {name}  Topic is Already in the Course!')
            return redirect('courseDetail', courseId=courseId) 
          else:
            topic = form.save(commit=False)
            topic.course = course
            topic.save()
            form.save_m2m()
            if request.method == 'POST' and 'save_and_continue' in request.POST:
                # Form submitted with "Save and Continue Editing" button
                show_modal = True
            else:
                show_modal = False
            messages.success(request, f'You have successfully created {name} for the {course.name}course.')
            url = reverse('courseDetail', args=[courseId]) + '?show_modal=true'
            # return redirect('courseDetail', courseId=courseId) 
            return redirect(url) 
      else:
          for field, errors in form.errors.items():
              for error in errors:
                  messages.warning(request, f'{error}')
  return render(request,'material/add_subTopic.html',{'form':form})


@login_required(login_url='logIn')
def createResource(request):
  form = ResourceForm()
  if request.method == 'POST':
   
      form = ResourceForm(request.POST, request.FILES)
      if form.is_valid():
          print("ssssss")
          name = form.cleaned_data.get('name')
          resource_type = form.cleaned_data.get('resource_type')
          url = form.cleaned_data.get('url')
          resourceExist = Resource.objects.filter(name= name, resource_type= resource_type, url=url)
          if resourceExist:
            messages.success(request, f'Sorry, {name} Resource is Already in the list!')
            url = request.POST.get('next', '/')
            return redirect(url)
          else:
            form.save()
            cId = request.POST.get('course')
            messages.success(request, f'You have successfully created {name} Resource.')
            # redirect_url = reverse('courseDetail', kwargs={'courseId': cId})
            url = request.POST.get('next', '/')
            return redirect(url)
            # return redirect('createSubTopic')
      else:
          for field, errors in form.errors.items():
              for error in errors:
                  field_label = form.fields[field].label if field in form.fields else field
                  print(field_label)
                  messages.warning(request, f'{field_label}: {error}')
          cId = request.POST.get('course')
          redirect_url = reverse('courseDetail', kwargs={'courseId': cId})
          url = request.POST.get('next', '/')
          return redirect(url)
  messages.warning(request, f'Page not found')
  return redirect('index')



@login_required(login_url='logIn')
def resourceList(request):
  # courses = Course.objects.prefetch_related('resources').all()
  resources = Resource.objects.all()
  return render(request, 'material/resource_list.html', {'resources': resources})



@login_required(login_url='logIn')
def resourceDetail(request,resourceId):
 # course = Course.objects.prefetch_related('resources').get(id= courseId)
  resource = Resource.objects.get(id= resourceId)
  if request.method == 'POST':
      form = EditResourceForm(request.POST, request.FILES,instance=resource)
      if form.is_valid():
          form.save()
          name = form.cleaned_data.get('name')
          messages.success(request, f'You have successfully Updated {name} Rsource.')
          return redirect('resourceList')
      else:
          for field, errors in form.errors.items():
              for error in errors:
                  messages.warning(request, f'{error}')
          return redirect('resourceDetail', resourceId=resourceId) 
  else:
    form = EditResourceForm(instance= resource)
  context = {'form':form,'resource': resource} 
  return render(request,'material/resource_detail.html',context)



@login_required(login_url='logIn')
def removeResource(request,resourceId):
  resource = Resource.objects.get(id = resourceId)
  resource.delete()
  messages.success(request, f'You have successfully Removed {resource.name} resource.')
  return redirect('resourceList')


@login_required(login_url='logIn')
def subTopicDetail(request,subTopicId):
 # course = Course.objects.prefetch_related('resources').get(id= courseId)
  topic = Topic.objects.get(id= subTopicId)
  if request.method == 'POST':
      form = EditSubTopicForm(request.POST, instance=topic)
      if form.is_valid():
          form.save()
          name = form.cleaned_data.get('name')
          messages.success(request, f'You have successfully Updated {name} Topic.')
          url = request.POST.get('next', '/')
          return redirect(url)
      else:
          for field, errors in form.errors.items():
              for error in errors:
                  messages.warning(request, f'{error}')
          url = request.POST.get('next', '/')
          return redirect(url)
  else:
    form = EditSubTopicForm(instance= topic)
    rform = ResourceForm()
  course = Course.objects.get(id= topic.course.id)
  context = {'form':form,'topic': topic,'rform':rform,'course':course} 
  return render(request,'material/subTopic_detail.html',context)

 
 
@login_required(login_url='logIn')
def removeSubTopic(request,subTopicId):
  topic = Topic.objects.get(id= subTopicId)
  course = Course.objects.get(id= topic.course.id)
  topic.delete()
  messages.success(request, f'You have successfully Removed {topic.name} Topic.')
  return redirect('courseDetail', courseId=course.id) 


def courseView (request,courseId):
  page = 'topic'
  # if order:
  #   topic = Topic.objects.get(course__id = courseId, order = order)
  # else:
  print(courseId)
  
  topic = get_object_or_404(Topic, course__id = courseId, order = 1 )
  # topic = Topic.objects.get(course__id = courseId, order = 1)
  topics = Topic.objects.filter(course__id = courseId)
  course = Course.objects.get(id= courseId)
  context = {'topics':topics,'course': course,'topic':topic, 'page':page} 
  return render(request,'users/topic_view.html',context)

def topicView (request,topicId):
  page= 'topic'
  topic = Topic.objects.get(id = topicId)
  order = topic.order
  course = topic.course
  topics = Topic.objects.filter(course= course)
  direction = request.GET.get('direction')
  if direction:
    if direction == 'prev':
      order-=1
      while True:
          topic_exists = Topic.objects.filter(course=course, order=order).exists()

          if topic_exists:
              # The topic exists
              topic = get_object_or_404(Topic, course=course, order=order)
              # topic = Topic.objects.get(course= course, order= order)
              break  
          else:
              order-=1
    elif direction == 'next':
      order+=1
      while True:
          topic_exists = Topic.objects.filter(course=course, order=order).exists()

          if topic_exists:
              # The topic exists
              topic = get_object_or_404(Topic, course=course, order=order)
              # topic = Topic.objects.get(course= course, order= order)
              break  
          else:
              order+=1
  context = {'topic':topic, 'topics':topics,'page':page } 
  return render(request,'users/topic_view.html',context)




def index(request):
  page='index'
  context= {
    'page':page
  }
  return render(request,'users/topic_view.html',context)