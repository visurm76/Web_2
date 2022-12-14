from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import UserForm

def index(request):
    if request.method == "POST":
        name = request.POST.get ("name") # получить значение поля Имя
        age = request.POST.get("age") # получить значение поля Возраст
        output = "<h2>Пользователь</h2><h3>Имя - {О},Возраст - {l}</hЗ>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request,"firstapp/index.html", {"form": userform})

def about(request):
    return render(request, "firstapp/about.html")

