from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
