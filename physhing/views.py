from django.shortcuts import render
from .forms import insta
from django.contrib import messages
from .models import user
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
    if request.method == 'POST':
        fm=insta(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            messages.success(request,'ACCOUNT CREATE SUCESSFULLY')
            fm.save(commit=False)
            return HttpResponseRedirect(request,'blog/server.html')
    else:
        fm=insta()
    return render(request,'blog/index.html',{'form':fm})



def server(request):
    return render(request,'blog/server.html')
