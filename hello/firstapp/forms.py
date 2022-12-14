from django import forms

class UserForm (forms.Form):
    name = forms.CharField(label="Имя миента",widget=forms.TextInput(attrs={"class":"myfield"}))
    age = forms.IntegerField(label="Boзpacт клиента", widget=forms.NumberInput(attrs={"class":"myfield"}))