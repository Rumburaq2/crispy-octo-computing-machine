from django.shortcuts import render

# Create your views here. //request handler

from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    #return HttpResponse("hello world")
    return render(request, 'hello.html', {'name': 'pero'})