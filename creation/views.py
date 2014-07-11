from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from creation.forms import EmailUserCreationForm
from creation.models import *

# Create your views here.
def stories(request):
    data = {
        'nodes': Branch.objects.all()
    }
    return render(request, "stories.html", data)

@login_required
def profile(request):
    return render(request, "profile.html")

def home(request):
    return render(request, "home.html")


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

def view_branch(request, branch_id):
    data = {
        'branch': Branch.objects.get(id=branch_id)
    }
    return render(request, "view_branch.html", data)