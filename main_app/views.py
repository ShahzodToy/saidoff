from django.shortcuts import render
from .api.serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class WhyUsView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WhyUsSerializer
    queryset = WhyUs.objects.all()


class PartnersView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PartnersSerializer
    queryset = Partners.objects.all()


class TeamView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class CertificateView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()


class FeedBackView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedBackSerializer
    queryset = FeedBack.objects.all()


class FAQView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FAQSerializer
    
    def get_queryset(self):
        page = self.kwargs.get('faq_page')
        if not FAQCategory.objects.filter(title=page).exists():
            raise ValidationError({'message': 'Not available with this title'})
        
        return FAQ.objects.filter(faq_page__title=page)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    

class PricePlanView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = (PricePlanSerializer)
    queryset = PricePlan.objects.all()

