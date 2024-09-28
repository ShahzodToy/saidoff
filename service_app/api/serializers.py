from rest_framework import serializers
from ..models import *
from .serializers import *



class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id','title','category_service')


class ServiceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryService
        fields = ('id','title')

class ServiceDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceDescription
        fields = ('id','service','title','description','image')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','name','phone_number','service_name','message','is_checked')

    
class PortfolioSerializer(serializers.ModelSerializer):
    
    service_name = serializers.CharField(source='service_name.title')
    
    class Meta:
        model = Portfolio
        fields = ('id','image', 'url_link', 'service_name','tags')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','title')
