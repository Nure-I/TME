from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)
  

class RegisterForm(UserCreationForm):
  
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm','placeholder': 'Email address'}))
    first_name = forms.CharField(max_length=30, label="",widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ','placeholder':'first Name'}))
    last_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ','placeholder': 'Last Name'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control-sm '}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control-sm '}))

    class Meta:
      model = User
      fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__ (self, *args, **kwargs):

      super(RegisterForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control form-control-sm'
      self.fields['username'].widget.attrs['placeholder'] = 'User Name'
      self.fields['username'].label = ''
      self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

      self.fields['password1'].widget.attrs['class'] = 'form-control form-control-sm'
      self.fields['password1'].widget.attrs['placeholder'] = 'Password'
      self.fields['password1'].label = ''
      self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

      self.fields['password2'].widget.attrs['class'] = 'form-control form-control-sm'
      self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
      self.fields['password2'].label = ''
      self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match.")

    # def save(self):
    #     username = self.cleaned_data['username']
    #     email = self.cleaned_data['email']
    #     first_name = self.cleaned_data['first_name']
    #     password = self.cleaned_data['password']

    #     user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
    #     return user
