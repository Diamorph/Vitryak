from django.shortcuts import render
from .models import Dish
# Create your views here.


def Main(request):
    if request.method == "GET":
        return render(request,"main.html")


def Garnish(request):
    if request.method == "GET":
        return render(request,"garnish.html",{'dishes':Dish.objects.all()})


def Dishes(request):
    if request.method == "GET":
        return render(request,"dish.html",{'dishes':Dish.objects.all()})


def Add(request):
    result = "Successful add!"
    if request.method == "POST" and  request.POST['name'] and request.POST['description'] and request.POST['weight'] and request.POST['price'] and request.POST['type'] :
        #form = Restaurants_Form(request.POST, request.FILES)
        Dish.objects.create(name=request.POST['name'],
                                     description=request.POST['description'],
                                     weight=request.POST['weight'],
                                     price=request.POST['price'],
                                     type=request.POST['type'])
        return render(request,"main.html", {'result': result})
    else:
        if request.method == "GET":
             return render(request,"add.html", {'dishes': Dish.objects.all()})


def Delete(request,id):
    result = "Successful del"
    if request.method == "POST":
        Dish.objects.get(id=int(id)).delete()
        return render(request,"main.html", {'result': result})



def Dishes_id(request,id):
    if request.method == "GET":
        return render(request,"dish.html" , {'dishes': [Dish.objects.get(id = int(id))]})
