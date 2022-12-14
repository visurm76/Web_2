from django import forms


class UserForm(forms.Form):
    vyb = forms.NullBooleanField(label="Bы поедете в Сочи этим летом?")
