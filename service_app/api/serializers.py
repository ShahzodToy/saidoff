from rest_framework import serializers
from ..models import *
from .serializers import *



class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('title',)


class ServiceDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceDescription
        fields = ('service','title','description','image')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    
class PortfolioSerializer(serializers.ModelSerializer):
    
    service_name = serializers.CharField(source='service_name.title')
    
    class Meta:
        model = Portfolio
        fields = ['image', 'url_link', 'service_name','tags']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)
