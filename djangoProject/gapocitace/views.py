from os import path

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here. request handler

def device_info(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World! at GA</h1>")
    #return render(request, 'home.html')

