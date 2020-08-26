from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Userregisterform,Profile_form
# Create your views here.

def home(request):
    return render(request,"employee/home.html")

def register(request):
    if request.method=="POST":
        form =Userregisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            messages.success(request,f"{username} account is created")
            return redirect("home")
    else:
        form=Userregisterform()

    return render(request,"employee/register.html",{"form":form}
                  )

def profile(request):
    if request.method == 'POST':
        form = Profile_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = Profile_form()
    return render(request, "employee/profile.html", {
        "form": form
    })

