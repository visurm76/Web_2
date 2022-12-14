from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import UserForm


def index(request):
    userform = UserForm(field_order=["age", "name"])
    return render(request, "firstapp/index.html", { "form": userform})

