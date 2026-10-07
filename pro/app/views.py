from textwrap import dedent

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



# Function Based

def Home(request):

    if(request.method=="GET"):

        return HttpResponse("Welcome To Django")

def Index(request):
    if (request.method=='GET'):
        return HttpResponse("Index")