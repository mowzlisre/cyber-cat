from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

@login_required
def home(request):
    context = {
        "subjects": Subject.objects.all(),
    }
    return render(request, 'app/dashboard.html', context)

@login_required
def classes(request, pk):
    subject = Subject.objects.get(sub_name=pk)
    context = {
        "subjects": Subject.objects.all(),
        "subject": subject,
    }
    return render(request, 'app/subject.html', context)

@login_required
def tutorials(request, pk, id):
    tutorial = Tutorials.objects.get(id=id)
    subject = Subject.objects.get(sub_name=pk)
    context = {
        "subjects": Subject.objects.all(),
        "subject": subject,
        "tutorial": tutorial
    }
    return render(request, 'app/tutorials.html', context)

