from django.urls import path
from .views import *

urlpatterns = [
    path('why-us',WhyUsView.as_view()),
    path('partners',PartnersView.as_view()),
    path('team',TeamView.as_view()),
    path('subscribe',SubscribeView.as_view()),
    path('certificate',CertificateView.as_view()),
    path('feedback',FeedBackView.as_view()),
    path('faq/<str:faq_page>/', FAQView.as_view(), name='faq-view'),
    path('priceplan',PricePlanView.as_view()),
]