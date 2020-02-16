from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings

from django.db.models import Q

from itertools import chain
from .models import ProductType, Shoe, Skirt, Bag

from .utils import sortProductsCats

def index(request):
    cats = ProductType.objects.all()
    shoes = Shoe.objects.all()[:4]
    skirts = Skirt.objects.all()[:4]
    bags = Bag.objects.all()[:4]
    
    # print(sortProductsCats(cats, shoes, skirts, bags))    

    context = {
        "productCats" : sortProductsCats(cats, shoes, skirts, bags),
        # "shoes" : shoes,
        "cats" : cats
    }
    # print(context)
    return render(request, 'ff/index.html', context)

def cat(request, cat_id):
    # productsOfptype = ProductType.objects.filter(pk=cat_id)
    cats = ProductType.objects.all()
    l = {
        2 : Shoe.objects.all,
        3 : Skirt.objects.all,
        4 : Bag.objects.all
    }
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
    cats = ProductType.objects.all()
    l = {
        2 : Shoe.objects.all,
        3 : Skirt.objects.all,
        4 : Bag.objects.all
    }
    productsOfptype = l[cat_id]()
    cat = productsOfptype[0].productType.typeName
    product = productsOfptype.filter(pk=p_id).values()[0]
    context = {
        "product" : product,
        "cats" : cats,
        "cat" : cat
    }
    return render(request, 'ff/product.html', context)


# # def search(request):
# #     form = q(request.GET)
# #     if form.is_valid():
# #         query = form.cleaned_data['q']
# #     video = Video.objects.filter(pk=query)
# #     print(query)
# #     context = {
# #         "video" : video,
# #     }
# #     return render(request, 'vidboard/watch.html', context)
# class VideoListCreate(generics.ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer

