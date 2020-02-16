from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings

from django.db.models import Q

from itertools import chain
from .models import ProductType, Shoe, Skirt, Bag

from .utils import sortProductsCats

l = {
    2 : Shoe.objects.all,
    3 : Skirt.objects.all,
    4 : Bag.objects.all
}

# This is hardcoded
sizes = {
    0 : {
        "name" : "8.0",
        "avail" : True
    },
    1 : {
        "name" : "8.5",
        "avail" : True
    },
    2 : {
        "name" : "9.0",
        "avail" : True
    },
    3 : {
        "name" : "9.5",
        "avail" : False
    },
    4 : {
        "name" : "10.0",
        "avail" : True
    },
    5 : {
        "name" : "10.5",
        "avail" : True
    },
    6 : {
        "name" : "11.0",
        "avail" : False
    },
    7 : {
        "name" : "11.5",
        "avail" : True
    },
    8 : {
        "name" : "12.0",
        "avail" : True
    }
}

cats = ProductType.objects.all()

    

def index(request):
    shoes = Shoe.objects.all()[:4]
    skirts = Skirt.objects.all()[:4]
    bags = Bag.objects.all()[:4]
    
    print(sortProductsCats(cats, shoes, skirts, bags))    

    context = {
        "productCats" : sortProductsCats(cats, shoes, skirts, bags),
        # "shoes" : shoes,
        "cats" : cats
    }
    # print(context)
    return render(request, 'ff/index.html', context)

def cat(request, cat_id):
    productsOfptype = l[cat_id]()   
    cat = productsOfptype[0].productType.typeName
    context = {
        "products" : productsOfptype,
        "cats" : cats,
        "cat" : cat
    }
    return render(request, 'ff/cat.html', context)

def product(request, cat_id, p_id):
    # productsOfptype = ProductType.objects.filter(pk=cat_id)
    shoeSizes = 0
    productsOfptype = l[cat_id]()
    cat = productsOfptype[0].productType.typeName
    # product = productsOfptype.filter(pk=p_id).values()[0]
    if cat == "Shoes":
        shoeSizes = sizes
    product = productsOfptype.filter(pk=p_id)[0]
    context = {
        "products" : productsOfptype[1:5],
        "product" : product,
        "cats" : cats,
        "cat" : cat,
        "sizes" : shoeSizes,
        "up" : ".."
    }
    return render(request, 'ff/product.html', context)

