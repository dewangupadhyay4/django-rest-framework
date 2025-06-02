from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)
