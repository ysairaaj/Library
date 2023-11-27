from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
# Create your views here. 


def login_page(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request , 'Username does not exist')
            return redirect('/register_page/') 
        
        user = authenticate(username = username , password = password)

        if user is None :
            messages.error(request , 'Invalid Username or password')
            return redirect('/login_page/') 
        
        else :
            login(request ,user)
            return redirect('/')



    return render(request , "accounts/login_page.html")  



def logout_page(request):
    print("trying to logout")
    logout(request)
    return redirect('/login_page/')

def register_page(request):
    if request.method == "POST" :
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       username = request.POST.get('username')
       password = request.POST.get('password') 

       user = User.objects.filter(username=  username)

       if user.exists() :
           messages.info(request , 'Username already taken')
           return redirect('/register_page/')

       print(first_name , last_name , username , password)
       user = User.objects.create( first_name = first_name , last_name = last_name , username = username)
       user.set_password(password)
       user.save()

       messages.info(request , 'Account created successfully') 
       return redirect('/login_page/')

    return render(request , "accounts/register_page.html")  
