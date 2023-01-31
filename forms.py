from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов", required=False)
    age = forms.IntegerField(label="Возраст клиента", required=False)
    basket = forms.BooleanField(label="Положить товар в корзину", required=False)
    vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")
    email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @")