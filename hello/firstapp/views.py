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
    cat = ["Ноутбук", "Принтеры", "Сканеры"]
    return render(request, "firstapp/index.html", context={"cat": cat})

def about(request):
    return render(request, "firstapp/about.html")

