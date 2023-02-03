from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse
from forms import UserForm


# Create your views here.
def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            return HttpResponse("<h2>имя введено корректно - {0}</h2>".format(name))
        else:
            return HttpResponse('Ошибка ввода данных')
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})

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