from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import RegisterForm , ProfileForm
from material.forms import FeedbackForm
from django.contrib.auth.models import User
from material.models import Course,Resource,Topic,Feedback
from .models import Profile
# Create your views here.


def index(request):
    form = FeedbackForm()
    course = Course.objects.count()
    resource = Resource.objects.count()
    topic = Topic.objects.count()
    users = Profile.objects.count()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for Your Time And Comments.')
            return redirect('index')
    context  ={ 'course':course,'resource':resource,'topic':topic,'users':users, 'fform':form}
    return render(request,'index.html',context)

def register(request):
    page = 'register'
    form = RegisterForm()
    pform = ProfileForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        pform = ProfileForm(request.POST)
        if form.is_valid() and pform.is_valid():
            user = form.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)  
            messages.success(request, f'Account created for {username}. You are now logged in.')
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{error}')
   
       

    return render(request, 'account/log_in.html', {'rform': form,'page':page,'pform':pform})


# @login_required
def logIn(request):
  page='logIn'
  if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('index')  # Replace 'home' with the name of your home page URL pattern
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('logIn')  
  else:
        form = AuthenticationForm()
  return render(request, 'account/log_in.html',{'form': form,'page':page})


@login_required(login_url='logIn')
def editProfile(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            login(request, User.objects.get(id=request.user.id) )
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')  # Redirect to the user's profile page
        else:
            messages.error(request, 'Error updating your profile. Please correct the errors below.')
    else: 
        form = RegisterForm(instance=request.user)

    return render(request, 'account/edit_profile.html', {'form': form})


def logOut(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

@login_required(login_url='logIn')
def userList(request):
    users = Profile.objects.filter(user__is_superuser=False)
    context  ={ 'users':users}
    return render(request,'account/list_of_users.html',context)


@login_required(login_url='logIn')
def feedBack(request):
    feedbacks = Feedback.objects.all()
    context  ={ 'feedbacks':feedbacks}
    return render(request,'account/feedback.html',context)