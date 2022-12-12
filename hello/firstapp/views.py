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
    data = {"age": 66}
    return render(request, "firstapp/index.html", context=data)

def about(request):
    return render(request, "firstapp/about.html")

