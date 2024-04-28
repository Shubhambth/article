from django.shortcuts import render , redirect
from .models import News,ContactData,AdminPost
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.contrib.auth.decorators import login_required
from . import forms


def savedata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = ContactData(name=name,phonenumber=phone,email=email,message=message)
        data.save()
        news = News.objects.all()
    return render(request,'index.html', {'news':news})


def home(request):
    news = News.objects.all()
    return render(request,'index.html' , {'news':news})










def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:    
        return render(request,'login.html')




def logout_user(request):
    logout(request)
    return redirect('home')




    
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            return redirect('register')
    else:

        return render(request,'register.html',{'form':form}) 
    




@login_required(login_url='login')
def detail(request,pk):
    news = News.objects.get(id=pk)
    return render(request,'detail.html',{'news':news})






@login_required(login_url='login')
def newpost(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.users = request.user
            form.save()
            return redirect('newpost')
    else:
        form = forms.CreatePost()
    return render(request,'addnews.html',{'form':form})
   