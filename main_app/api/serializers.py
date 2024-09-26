from rest_framework import serializers
from ..models import *
from django.utils.translation import get_language

class WhyUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhyUs
        fields = ( 'title','description' )


class PartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partners
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('image', 'title','description')


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = ('comment','name','image','profession')

    
class FAQCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQCategory
        fields = "__all__"

class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ('faq_page','answer','question')



class PricePlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PricePlan
        fields = ('title','limit_date','limit_user','features')

 


class FeaturesSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('title','tick')