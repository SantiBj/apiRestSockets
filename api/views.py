from django.shortcuts import render
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your views here.

class CustomerListAPIView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    
    def get(self,request,**kwargs):
        try:
            customer = Customer.objects.get(id=kwargs["id"])
        except:
            return Response({"code":"404","message":"Customer not exists"},status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CustomerCreateAPIView(generics.CreateAPIView):

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #notificando al consumer del cambio
            channel_layer = get_channel_layer()
            newRecord = serializer.data
            
            async_to_sync(channel_layer.group_send)(
                'customer',{"type":"newCustomer","data":json.dumps(newRecord)}
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"code":"406","message":"data not valid"},status=status.HTTP_406_NOT_ACCEPTABLE)