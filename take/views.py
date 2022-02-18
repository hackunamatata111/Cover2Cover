

from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .models import Take,Profile
from django.db.models import Q
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from .forms import SignUpForm



def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mob':user.profile.mob,'name':user.profile.name,'cname':user.profile.cname,})

def loginpage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')    

    context={}
    return render(request, 'take/loginpage.html', context)
@login_required(login_url='login')    
def logoutuser(request):
    logout(request)
    return redirect('landing')

def register(request):
    form=SignUpForm(request.POST)
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.mob = form.cleaned_data.get('mob')
            update_user_data(user) 
            user.profile.name = form.cleaned_data.get('name')
            update_user_data(user) 
            user.profile.cname = form.cleaned_data.get('cname')
            update_user_data(user) 
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user=authenticate(username=user.username, password=raw_password)
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request,'take/register.html',{'form':form})


@login_required(login_url='login')
def home(request):
    context={}
    return render(request, 'take/home.html', context)
@login_required(login_url='login')
def takehome(request):
    k=request.user.profile.cname
    q=request.GET.get('q') if request.GET.get('q') !=None else''
    takes= Take.objects.filter(
        (Q(name__icontains=q) |
        Q(auth__icontains=q) |
        Q(course__icontains=q) |
        Q(description__icontains=q)) &
        Q(cname__icontains=k)
        )
    take_count= takes.count()
    context={'takes': takes, 'take_count': take_count}
    return render(request, 'take/takehome.html',context)
@login_required(login_url='login')
def info(request, pk):
    take=Take.objects.get(id=pk)
    if take.mob==None:
        cmn=False
    else:
        cmn=True
    if take.contact==None:
        cem=False
    else:
        cem=True            
    context={'cem': cem, 'take':take, 'cmn': cmn}
    return render(request, 'take/info.html', context)
@login_required(login_url='login')
def post(request):
    form=BookForm()
    if request.method =='POST':
        form=BookForm(request.POST)
        mnc=request.POST.get('mn')
        emc=request.POST.get('em')
        
        if mnc=='on':
            mn=request.user.profile.mob
        else:
            mn=None
        if emc=='on':
            em=request.user
        else:
            em=None 
        if form.is_valid():

            Take.objects.create(
                roll=request.user,
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                auth=request.POST.get('auth'),
                contact=em,
                mob=mn,
                course=request.POST.get('course'),
                cname=request.user.profile.cname,
            )

            return redirect('redirectt')
    context={'form': form}
    return render(request, 'take/post.html', context)

def landing(request):
    return render(request, 'take/landing.html')

@login_required(login_url='login')
def profile(request):
    q=request.user
    takes=Take.objects.filter(roll=q)

    context={
        'User':request.user,
        'takes':takes
    }

    return render(request, 'take/profile.html', context)

@login_required(login_url='login')

def updateBook(request, pk):
    take=Take.objects.get(id=pk)
    form=BookForm(instance=take)
    updatetitle=True
    if take.mob !=None:
        ccmn=True
    else:
        ccmn=False
    if take.contact !=None:
        ccem=True
        
    else:
        ccem=False    

    if request.method =='POST':
        form=BookForm(request.POST, instance=take)
        mnc=request.POST.get('mn')
        emc=request.POST.get('em')
       
        if mnc=='on':
            mn=request.user.profile.mob
        else:
            mn=None
        if emc=='on':
            em=request.user
        else:
            em=None 
        if form.is_valid():

            Take.objects.filter(id=pk).update(
                roll=request.user,
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                auth=request.POST.get('auth'),
                contact=em,
                mob=mn,
                course=request.POST.get('course'),
                cname=request.user.profile.cname,
            )
            return redirect('profile')                 
    context={'form': form, 'take':take, 'ccem':ccem, 'ccmn':ccmn, 'updatetitle': updatetitle}
    return render(request, 'take/post.html', context)

            
@login_required(login_url='login')
def deleteBook(request, pk):
    take=Take.objects.get(id=pk)
    if request.method=='POST':
        take.delete()
        return redirect('profile')  
    return render(request, 'take/delete.html') 

@login_required(login_url='login')
def redirectt(request):
    context={}
    return render(request, 'take/redirect.html', context)
@login_required(login_url='login')
def edit(request):
    context={}
    return render(request, 'take/edit.html', context)
