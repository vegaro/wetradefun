from django import forms
from django.core import validators
from django.contrib.auth.models import User
 
class RegistrationForm(forms.Form):
  """ 
  Form for creating new login
  """
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  check_password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    try:
      if self.cleaned_data['password'] != self.cleaned_data['check_password']:
        raise forms.ValidationError("Passwords entered do not match")
      if self.cleaned_data['email'] and User.objects.filter(email=self.cleaned_data['email']).exclude(username=self.cleaned_data['username']).count():
        raise forms.ValidationError("Email addresses must be unique.")
      if self.cleaned_data['username'] and User.objects.filter(username=self.cleaned_data['username']).exclude(email=self.cleaned_data['email']).count():
        raise forms.ValidationError("Usernames must be unique.")
    except KeyError:
      # didn't find what we expected in data - fields are blank on front end.  Fields
      # are required by default so we don't need to worry about validation
      pass
    return self.cleaned_data

class SearchForm(forms.Form):
  query = forms.CharField()