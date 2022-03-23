from django.http import request
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import View
# Create your views here.

class UserFormView(View):
    form_class=UserRegisterForm
    template_name='user/registration_form.html'
    
    # Get empty form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

# process form data
    def post(self,request):
        form=self.form_class(request.POST)
        
        if form.is_valid():
            
            user=form.save(commit=False)
            
            # cleaned (normalized) data
            
        
