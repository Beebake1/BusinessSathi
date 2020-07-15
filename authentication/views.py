from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request,'authentication/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

def register(request):
    user_form = CreateUserForm()
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST,request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            user_profile = UserProfile.objects.create(user=user,image=user_form.cleaned_data['image'])
            return redirect('authentication:user_index')
    context = {
        'user_form':user_form,
        'title':'User'
    }
    return render(request,'authentication/register.html',context)

def change_password(request):
    form = UserPasswordChangeForm()
    context = {
        'user_form':form,
        'title':'Change Password'
    }
    return render(request,'authentication/register.html',context)

def user_update(request,id):
    user_profile = UserProfile.objects.get(id=id)
    user = User.objects.get(id=user_profile.user.id)
    form = UserUpdateForm(instance = user)
    profile_form = UserProfileForm(instance = user_profile)
    form.fields['image'].initial = user_profile.image
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            if form.cleaned_data['image'] != None:
                user_profile.image = form.cleaned_data['image']
                user_profile.save()
            return redirect('authentication:user_index')
    context = {
        'user_form':form,
        'title':'User'
    }
    return render(request,'authentication/register.html',context)  


def home(request):
    context = {
        'title':'Dashboard',
    }
    return render(request,'home/index.html',context=context)

def user_list(request):
    context = {
        'title':'User',
        'users': UserProfile.objects.all(),
    }
    print(User.objects.all())
    return render(request,'authentication/index.html',context=context)

def group_index(request):
    context = {
        'title':'Group',
        'groups': Group.objects.all(),
    }
    return render(request,'authentication/group/index.html',context=context)

def permission_index(request):
    context = {
        'title':'Permission',
        'group': Permission.objects.all(),
    }
    return render(request,'authentication/permission/index.html',context=context)

def group_create(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authentication:group_index')
    context = {
        'title':'Group',
        'form': form,
    }
    return render(request,'authentication/group/create.html',context=context)

def group_update(request,id):
    group = Group.objects.get(id=id)
    form = GroupForm(instance=group)
    if request.method == 'POST':
        form = GroupForm(request.POST,instance=group)
    if form.is_valid():
        form.save()
        return redirect('authentication:group_index')
    context = {
        'title':'Group',
        'form': form,
    }
    return render(request,'authentication/group/create.html',context=context)
