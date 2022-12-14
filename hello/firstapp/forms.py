from django import forms


class UserForm(forms.Form):
    basket = forms.BooleanField(label="Пoлoжить товар в корзину")
