from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.


def index(request):
    return HttpResponse("OK")