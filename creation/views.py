from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
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

@login_required
def view_branch_vote(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    # branches = Branch.objects.all()
    # data = {
    #     'branches': branches
    # }
    try:
        Vote.objects.get(writer_vote=request.user, branch_vote=branch)
    except Vote.DoesNotExist:
        vote = Vote.objects.create(writer_vote=request.user, branch_vote=branch)
        vote.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def leaderboard(request):
    # branch = Branch.objects.get(id=27)
    stuff = ""
    branches = Branch.objects.all()
    path_votes = []
    for branch in branches:
        if branch.is_leaf_node():
            votes = 0
            path = branch.get_ancestors(include_self=True)
            for thing in path:
                votes += thing.branch_votes.all().count()
            path_votes.append([branch, votes])
    # after that, path_votes should now include a list of nested lists of [child nodes: sum of all votes up it's path']
    branch_most_votes = max(path_votes, key=lambda x: x[1])
    ancestor_branches = branch_most_votes[0].get_ancestors(include_self=True)
    data = {
        'branches': ancestor_branches
    }

    return render(request, "view_story_path.html", data)


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