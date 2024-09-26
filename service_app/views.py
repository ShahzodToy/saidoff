from django.shortcuts import render
from .api.serializers import *
from .models import *
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class ServiceView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceDescriptionView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request, pk):

        service = Service.objects.get(id = pk)

        service_desc = ServiceDescription.objects.filter(service = service.id)
        serializer = ServiceDescriptionSerializer(service_desc,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

class OrderView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    

class PortfolioListView(ListAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        service_id = self.kwargs.get('service_id')
        if service_id:
            if not Service.objects.filter(id=service_id).exists():

                return Portfolio.objects.filter(service_name=service_id)
            
        return Portfolio.objects.all()


    
    


    