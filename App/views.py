from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from .models import Category, Product

from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def Home(request):
    return render(request, 'App/home.html')

def CategoriesView(request):
    c = Category.objects.all()
    return render(request, 'App/categories.html', {'c':c})


def CatProductView(request, prod_id):
    p = Product.objects.filter(prod_id = prod_id)
    print(p)

    return render(request, 'App/home.html', {'p': p})


####   API VIEWS  ####
@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def createCat(request):

#########  EXTRA VIEWS   #########
    url = 'https://chittiv3.vistannextgen.co.uk/api/restarent.php'
    cat = requests.get(url, verify = False)
    cats = cat.json()
    print(len(cats))   

    for c in cats:
        print(c['id'])
        c = Category.objects.create(
            cat_id = c['id'],
            category_name = c['category_name'],
        )
        c.save()

    return HttpResponse('Category data added')

