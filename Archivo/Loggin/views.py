from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Loggin.forms import FormSearch


# Create your views here.

def home(request):
    return render(request, "base/index.html")

def Sign(request):
    return render(request,"base/sign.html")

def SignIn(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass']
        

        user = authenticate(username = username, password = pass1)
        
        if user is not None:
            login(request,user)

            fname = user.get_username()
            return render(request, "base/index.html")

        else:
            messages.error(request, "Su cuenta no fue encontrada")    
            return redirect('home')
        


    return render(request, "base/index.html")

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
            return render(request, "base/index.html")
            

        if User.objects.filter(email=email):
            messages.error(request, "El email ya es usado por otra cuenta")
            return render(request, "base/index.html")


        if pass1 != pass2 :
            messages.error(request, "Las contrasenas no son iguales")
            return render(request, "base/index.html")
        
        if not username.isalnum():
            messages.error(request, "El nombre de usuario debe ser alfanumerico")
            return render(request, "base/index.html")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        

        myuser.save()
        user = authenticate(username = username, password = pass1)
        return render(request, "base/index.html")

    return render(request, "base/index.html")

def Search(request):
    searching = FormSearch()

    return render(request, "base/search.html", {"form": searching}) 