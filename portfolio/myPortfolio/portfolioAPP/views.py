from django.shortcuts import render

# Create your views here.

def portfolio (request):
    return render(request, 'index.html')

def contato (request):
    return render(request, 'contato.html')

def english (request):
    return render(request, 'english.html')