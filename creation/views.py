from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from creation.forms import EmailUserCreationForm, BranchForm, VoteForm
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

def view_story_path(request, branch_id):
    branches = Branch.objects.get(id=branch_id).get_ancestors(include_self=True)
    data = {
        'branches': branches
    }
    return render(request, "view_story_path.html", data)


@login_required()
def view_branch(request, branch_id):
    # writer = request.user
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            parent = Branch.objects.get(id=branch_id)
            user = request.user
            text = form.cleaned_data['text']
            Branch.objects.create(title=title, parent=parent,
                                  user=user, text=text)
            return redirect('stories')
    else:
        form = BranchForm()
    data = {
        'branch_form': form,
        'branch': Branch.objects.get(id=branch_id)}
    return render(request, "view_branch.html", data)

# def view_branch(request, branch_id):
#     user = request.user
#     if request.method == "POST":
#         form = BranchForm(request.POST)
#         if form.is_valid():
#             if form.save():
#                 return redirect("/stories")
#     else:
#         form = BranchForm()
#
#     data = {
#         'form': form,
#         'branch': Branch.objects.get(id=branch_id),
#     }
#     return render(request, "view_branch.html", data)