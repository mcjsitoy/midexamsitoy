from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
from .forms import CandidateModelForm
from datetime import datetime


# Create your views here.
def index(request):
    context = {}
    candidates = Candidate.objects.all()

    context['candidates'] = candidates
    return render(request,'index.html', context)

def addcandidate(request):
    context ={}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request,'addcandidate.html', context)
