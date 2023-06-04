from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def manu(request):
   return HttpResponse('<h1>this is specific url mapping<h1>')