from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateList
# Create your views here.


def index(response, id):
    ls =  ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            print("Created new ToDoList.")

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateList()
    return render(response, "main/create.html", {"form": form})
