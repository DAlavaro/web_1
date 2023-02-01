from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов", required=False)
    age = forms.IntegerField(label="Возраст клиента", required=False)
    basket = forms.BooleanField(label="Положить товар в корзину", required=False)
    vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")
    email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @", required=False)
    ip_adres = forms.GenericIPAddressField(label="IP адрес", help_text="Пример формата 192.0.2.0", required=False)
    reg_text = forms.RegexField(label="Text", regex="^[0-9][A-F][0-9]$",required=False)
    slug_text = forms.SlugField(label="Введите текст", required=False)
    url_text = forms.URLField(label="Введите URL", help_text="Например http://www.dalavaro.ga", required=False)
    uuid_text = forms.UUIDField(label="Введите UUID", help_text="Формат xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", required=False)
    combo_text = forms.ComboField(label="Введите URL",
                                  fields=[forms.URLField(),
                                          forms.CharField(max_length=20)])

