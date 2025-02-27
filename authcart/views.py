from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if(request.method == 'POST'):
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.error(request,"Password is not Matching")
            return redirect("signup")
        try:
            if User.objects.get(username=email):
                messages.info(request,"Email already Exist")
                return render(request, 'signup.html')
        except Exception as identifier:
            pass
        user= User.objects.create_user(email,email,password)
        user.save()
        messages.success(request,"User Created Successfully")
    return render(request, "signup.html")



def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass1')
        # check if user has entered correct credetials
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            # No backend authenticated the credentials
            return render(request, 'login.html')
        
    return render(request, "login.html")



def handlelogout(request):
    logout(request)
    messages.error(request, "Logout Success")
    return redirect("/auth/login")
