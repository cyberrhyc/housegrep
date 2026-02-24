from django.urls import path, include
from . import views as v 
urlpatterns=[
    path("", v.Home.homepage, name='home'),
    path("properties/", v.Properties.home, name='prophome'),
    path("propertiessearch/", v.Properties.search, name='propsearch'),
    path("login/", v.Auth.login, name='login'),
    path("signup/", v.Auth.signup, name='signup'),
    path("cprofile/", v.Auth.createProfile, name='profilecreate'),
    path("addprop/", v.Owner.addProperty, name='addprop'),
]