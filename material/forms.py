from django import forms
from .models import Course, Resource, Tag, Review, Topic, Feedback

class CourseForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Course Title or Name'}))
    description = forms.CharField(max_length=200, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'Descriptions'}))
    difficulty_level = forms.ChoiceField(choices=Course.DIFFICULTY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm ','placeholder': 'Choose Difficulty'}))
    
    class Meta:
        model = Course
        fields = ('name', 'description',  'difficulty_level')


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description','rating', 'difficulty_level','prerequisites','tags')

    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Course Title or Name'}))
    description = forms.CharField(max_length=200, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'Descriptions'}))
    #rating = forms.forms.FloatField(max_length=30, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'Descriptions'}))
    rating = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    difficulty_level = forms.ChoiceField(choices=Course.DIFFICULTY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm ','placeholder': 'Choose Difficulty'}))
    prerequisites = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm '}),required=False)
    #resources = forms.ModelMultipleChoiceField(queryset=Resource.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}),required=False)
    #reviews = forms.ModelMultipleChoiceField(queryset=Review.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm '}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm  '}),required=False)
    
    

class EditSubTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', 'course','resources','descriptions','order','url')

    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Course Title or Name'}))
    order = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Order Number For The Sub topic'}))
    resources = forms.ModelMultipleChoiceField(queryset=Resource.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}),required=False)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    url = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Youtube url'}),required=False)
    # descriptions = forms.CharField(max_length=200, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'Descriptions'}))
  

class SubTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', 'resources','descriptions','order')

    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Course Title or Name'}))
    order = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Order Number For The Sub topic'}))
    resources = forms.ModelMultipleChoiceField(queryset=Resource.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}),required=False)
    # descriptions = forms.CharField(max_length=200, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'Descriptions'}))
  

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('name', 'content','resource_type','file','url')

    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Course Title or Name'}))
    content = forms.CharField(max_length=200, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'content'}))  
    resource_type = forms.ChoiceField(label="",choices=Resource.RESOURCE_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm ','placeholder': 'Choose Difficulty'}))
    url = forms.CharField(max_length=200, label="",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ','placeholder':'UrlS'}))  
    file = forms.FileField(label="",widget=forms.ClearableFileInput(attrs={'class': ''}),required=True) 
    
class EditResourceForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'content','resource_type','file','url')
    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Course Title or Name'}))
    content = forms.CharField(max_length=200, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'content'}))  
    resource_type = forms.ChoiceField(choices=Resource.RESOURCE_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm ','placeholder': 'Choose Difficulty'}))
    url = forms.CharField(max_length=200, label="",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ','placeholder':'UrlS'}))  
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm custom-file-input'})) 
    

class FeedbackForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Your Name'}))
    email = forms.EmailField(max_length=200, label="", widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter your email'}))
    message = forms.CharField(max_length=200, label="",widget=forms.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder':'Yor Message here'}))  
    
    class Meta:
        model = Feedback
        fields = ('first_name', 'email',  'message')

