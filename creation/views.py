from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from creation.forms import EmailUserCreationForm
from creation.models import *

# Create your views here.
def show_branches(request):
    data = {
        'nodes': Branch.objects.all()
    }
    return render(request, "branches.html", data)

def profile(request):
    return render(request, "profile.html")


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form
    })