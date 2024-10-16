from django.http import HttpResponse
from django.shortcuts import render

def authentication2(request):
    return render(request, 'F2.html')

def authentication3(request):
    return render(request, 'F3.html')

def authentication6(request):
    return render(request, 'F6.html')
