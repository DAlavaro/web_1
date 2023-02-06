from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from firstapp.models import Person


# Получение данных из БД и загрузка index.html
def index(request):
    people = Person.objects.all()
    return render(request, "firstapp/index.html", {"people": people})


# Сохранение данных в БД
def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")


# Изменение данных в БД
def edit(request, id_):
    try:
        person = Person.objects.get(id=id_)
        
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "firstapp/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


# Удаление из базы данных
def delete(request, id_):
    try:
        person = Person.objects.get(od=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")

