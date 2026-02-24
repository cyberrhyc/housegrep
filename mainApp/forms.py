from django import forms
from .models import *


class SignUpForm(forms.Form):
    phonenumber = forms.CharField(label="Phone Number", max_length=100)
    IdNumber=forms.CharField(label="Id Number", max_length=20)
    password1=forms.CharField(label="Password", max_length=20)
    password2=forms.CharField(label="Confirm Password", max_length=20)
    
class ProfileCreation(forms.Form):
    UserTypes = [
    ("","--Pick a user type--"),
    ("T", " Tennant"),
    ("P", "Owner"),
]
    uytpe=forms.ChoiceField(choices=UserTypes)
    Name=forms.CharField(label='Your Name', max_length=50)
    

class LogInForm(forms.Form):
    username = forms.CharField(label="Id Number or Phone Number", max_length=100)
    password=forms.CharField(label="Password", max_length=20)

class AddPropertyForm(forms.ModelForm):
    Densities = [
    ("","--location density--"),
    ("L", " Low"),
    ("M", "Medium"),
    ("H", "High"),
]
    file=forms.FileField()
    Location = forms.CharField() 
    Density = forms.ChoiceField(choices=Densities)
    Rooms=forms.IntegerField()
    Features=forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

    class Meta:
        model = House
        fields = ['file', 'Location', 'Density','Rooms','Features']

    def save(self, commit=True):
        instance = super().save(commit=False)
       
        instance.Location = instance.Location.title()
        
        if commit:
            instance.save()
        return instance