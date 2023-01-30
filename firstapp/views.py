from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse
from forms import UserForm


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name") # получить значение поля Имя
        age = request.POST.get("age") # Получить значение поля Возраст
        output = "<h2> Пользователь </h2><h3>Имя - {0}, Возраст - {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", "1")
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)