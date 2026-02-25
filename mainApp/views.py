from django.shortcuts import render,redirect
from django.http import request
from . import forms
from . import models

# Create your views here.
class Home:
    def homepage(request):
        return render(request, "home.html" )
    
class Owner:
    def addProperty(request):
        print("hi")
        if request.method == 'POST':
            form=forms.AddPropertyForm(request.POST,request.FILES)
            if form.is_valid():
                form.save() 
                return redirect('home') 
        else:
            form = forms.AddPropertyForm(request.POST, request.FILES)

        return render(request,'owner/addproperty.html', {'form':form})


class Properties:
    def home(request):
        props=models.House.objects.all()
        print(props)
        return render(request, "properties.html",{'props':props})
    
    def search(request):
        return render(request, 'propsearch.html')
    
class Auth:
    def login(request):
        form=forms.LogInForm
        return render(request, 'auth/login.html', {'form':form})
    
    def signup(request):
        form=forms.SignUpForm
        return render(request, 'auth/signup.html',{'form':form})
    
    def createProfile(request):
        form=forms.ProfileCreation
         
        return render(request,"auth/createprofile.html", {'form':form})
    
    