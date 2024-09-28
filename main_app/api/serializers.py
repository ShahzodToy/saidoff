from rest_framework import serializers
from ..models import *


class WhyUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhyUs
        fields = ('id','title','description','image')


class PartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partners
        fields = ('id','image')

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id','name','profession','image')



class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('id','image', 'title','description')


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = ('id','comment','name','image','profession')

    
class FAQCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQCategory
        fields = ('id','title')

class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ('id','faq_page','answer','question')



class PricePlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PricePlan
        fields = ('id','title','limit_date','limit_user','features')

 


class FeaturesSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id','title','tick')