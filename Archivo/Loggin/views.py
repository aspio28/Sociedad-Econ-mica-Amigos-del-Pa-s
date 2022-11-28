from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, "base/index.html")

def SignIn(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass']
        

        user = authenticate(username = username, password = pass1)
        
        if user is not None:
            login(request,user)
            
            return render(request, "base/index.html", {'user': user})

        else:
            messages.error(request, "Su cuenta no fue encontrada")    
            return redirect('home')
        


    return render(request, "base/signin.html")

def SignOut(request):
    logout(request)
    messages.success(request, "Has salido de la cuenta de forma exitosa")
    return redirect('home')

def SignUp(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "El nombre de usuario ya existe")
            return render(request, "base/signup.html")
            

        if User.objects.filter(email=email):
            messages.error(request, "El email ya es usado por otra cuenta")
            return render(request, "base/signup.html")


        if pass1 != pass2 :
            messages.error(request, "Las contrasenas no son iguales")
            return render(request, "base/signup.html")
        
        if not username.isalnum():
            messages.error(request, "El nombre de usuario debe ser alfanumerico")
            return render(request, "base/signup.html")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Su cuenta ha sido creada correctamente")
        return render(request, "base/signin.html")

    return render(request, "base/signup.html")