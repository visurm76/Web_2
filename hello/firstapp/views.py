from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
from django.template.response import TemplateResponse

"""
def index(request):    
    return HttpResponse("Hello word! My first project django")
"""
"""__________Статичные файлы_______________________"""

def index(request):
    return render(request, "firstapp/index.html")

def about(request):
    return render(request, "firstapp/about.html")

