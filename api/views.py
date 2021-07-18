from django.http import response
from django.shortcuts  import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

from.sealiazers import productserializer
from .models import product
from api import sealiazers
"""
@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List': '/product_list/',
        'detail_view': '/product_detail/<int:id>',
        'create': '/product_create/',
        'update': '/product-update/<int:id>',
        'delete': '/product-delete/<int:id>',

    }
    return response(api_urls)
"""

@api_view(['GET'])
def ShowAll(request):
    products = product.objects.all()
    serializer = productserializer(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def viewproduct(request,ex):
    products = product.objects.get(id=ex)
    serializer = productserializer(products, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createproduct(request,ex):
    serializer = productserializer(data=request.data)
    Serializer.save()
    return Response(serializer.data)