from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone



class Dish(models.Model):

    BRAND_FOOD = 'фірмові_страви' # фірмова страва
    SALAD  = 'салат' #cалат
    COLD_SNECK = 'холодні_закуски' # холодна закуска
    HOT_SNECK = 'гарячі_закуски' #гаряча
    FIRST_DISH = 'перші_страви'
    SECOND_DISH = 'другі_страви'
    GARNISH = 'гарніри'
    PANCAKES = 'деруни' # деруни та гречаники
    TEA = 'чай'
    COFFE = 'кава'
    TYPE = (
        (BRAND_FOOD , 'фірмові_страви'),
        (SALAD , 'салат'),
        (COLD_SNECK , 'холодні закуски'),
        (HOT_SNECK , 'гарячі закуски'),
        (FIRST_DISH , 'перші страви'),
        (SECOND_DISH , 'другі страви'),
        (GARNISH , 'гарніри'),
        (TEA , 'чай'),
        (COFFE , 'кава'),
    )

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    weight = models.IntegerField()
    price  = models.IntegerField()
    type = models.CharField(max_length=30, choices=TYPE)
    #type = ArrayField(models.CharField(max_length=150, choices=TYPE), size=40 ,default=None)

    def __str__(self):
        return self.name

    def dict(self):
        return {'name' : self.name ,
                'description' : self.description,
                'weight' : self.weight,
                'price' : self.price,
                'types' : [i for i in self.type]
                }
# Create your models here.
