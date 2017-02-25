from django.shortcuts import render
from .models import Dish
# Create your views here.


def Main(request):
    if request.method == "GET":
        return render(request,"main.html")

def Dishes(request):
    if request.method == "GET":
        return render(request,"dish.html",{'dishes':Dish.objects.all()})

def Specialty(request):
    if request.method == "GET":
        return render(request,"specialty.html",{'dishes':Dish.objects.all()})

def Cold_snacks(request):
    if request.method == "GET":
        return render(request,"cold_snacks.html",{'dishes':Dish.objects.all()})

def Hot_snacks(request):
    if request.method == "GET":
        return render(request,"hot_snacks.html",{'dishes':Dish.objects.all()})

def First_courses(request):
    if request.method == "GET":
        return render(request,"first_courses.html",{'dishes':Dish.objects.all()})

def Garnish(request):
    if request.method == "GET":
        return render(request,"garnish.html",{'dishes':Dish.objects.all()})

def Main_dishes(request):
    if request.method == "GET":
        return render(request, "main_dishes.html", {'dishes': Dish.objects.all()})

def Vareniki(request):
    if request.method == "GET":
        return render(request, "vareniki.html", {'dishes': Dish.objects.all()})

def Desserts(request):
    if request.method == "GET":
        return render(request, "desserts.html", {'dishes': Dish.objects.all()})

def Alcohol(request):
    if request.method == "GET":
        return render(request, "alcohol.html", {'dishes': Dish.objects.all()})







def Add(request):
    result = "Successful add!"
    if request.user.is_superuser:
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
    if request.method == "POST" and request.user.is_superuser:
        Dish.objects.get(id=int(id)).delete()
        return render(request,"main.html", {'result': result})



def Dishes_id(request,id):
    if request.method == "GET":
        return render(request,"dish.html" , {'dishes': [Dish.objects.get(id = int(id))]})
