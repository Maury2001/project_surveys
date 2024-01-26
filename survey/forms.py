from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Survey, Project


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        if user:
            instance.users.add(user)

        return instance

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'required': False}),
            'checkin': DateInput(),
            'checkout': DateInput(),
        }
            
       
        