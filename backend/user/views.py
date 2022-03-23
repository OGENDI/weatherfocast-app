from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import View
# Create your views here.

class UserFormView(View):
    form_class=UserRegisterForm
