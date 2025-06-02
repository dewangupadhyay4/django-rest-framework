from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def get_items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializers = ItemSerializer(items, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ItemSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
