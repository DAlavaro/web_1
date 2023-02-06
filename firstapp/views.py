from django.http import HttpResponseRedirect
from django.shortcuts import render
from firstapp.models import Person


# Получение данных из БД и загрузка index.html
def index(request):
    people = Person.objects.all()
    return render(request, "firstapp/index.html", {"people": people})


def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")
