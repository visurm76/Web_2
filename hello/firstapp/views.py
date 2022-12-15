from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import Person

"""
def index(request):
    userform = UserForm(field_order=["age", "name"])
    return render(request, "firstapp/index.html", { "form": userform})
"""
# получение данных из БД и загрузка index.html
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

# сохранение данных в БД
def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")

