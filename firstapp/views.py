from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<H2>Главная</H2>")


def about(request):
    return HttpResponse("<H2>О сайте</H2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def products(request, productid = 1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id=1, name="Mikle"):
    output = "<h2>Пользватель</h2><h3>id: {0} Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)