from django.shortcuts import render
from django.http import HttpResponse

def teams_home(request):
    return HttpResponse("Teams app working!")
