from django.shortcuts import render
from .models import ItemMenu

# Create your views here.


def index(request):
    items = ItemMenu.objects.filter(active=True)
    britems = items.filter(category__engid="Breakfast")
    citems = items.filter(category__engid="Coffee")
    hitems = items.filter(category__engid="Herbal")
    sitems = items.filter(category__engid="Syrup")
    smitems = items.filter(category__engid="Smoothie")
    shitems = items.filter(category__engid="Shake")
    moitems = items.filter(category__engid="Mocktail")
    aps = items.filter(category__engid="Appetizer&Salad")
    pitems = items.filter(category__engid="Pasta")
    pnitems =items.filter(category__engid="Panini")
    pzitems = items.filter(category__engid="Pizza")
    plitems = items.filter(category__engid="Platter")
    ditems = items.filter(category__engid="Drink")
    hoitems = items.filter(category__engid="Hookah")
    bitems = items.filter(category__engid="Baked Sandwiches")
    ctx = {'title': "Agate Cafe - Menu", "britems": britems,
           "citems": citems, "hitems": hitems,
           "sitems": sitems, "smitems": smitems,
           "shitems": shitems, "moitems": moitems,
           'aps': aps, 'pitems': pitems, "pnitems": pnitems,
           "pzitems": pzitems, "plitems": plitems, "ditems": ditems, "hoitems": hoitems, "bitems": bitems}
    return render(request, 'blog/index.html', ctx)


