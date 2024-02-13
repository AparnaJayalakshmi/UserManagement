from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserUpdateForm,UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created for '+ user)
                return redirect('loginPage')
        context = {'form':form}
        return render(request,'signup.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request,'user logged in successfully for '+username)
                return redirect('home')
            else:
                messages.info(request,'username or password is incorrect')
        return render(request,'login.html')

def logoutUser(request):
    
    logout(request,)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def home(request):
    users = User.objects.all().order_by('id')
    context = {
        'users':users
    }
    return render(request,'home.html',context)


def createuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')  
    else:
        form = UserForm()
    return render(request, 'Createuser.html', {'form': form})

def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'update_user.html', {'form': form})
    

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        
        user.delete()
        messages.success(request, f"{user.username} deleted successfully.")
        return redirect('home')  
