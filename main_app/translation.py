from modeltranslation.translator import TranslationOptions, translator
from .models import WhyUs, Certificate,FeedBack,FAQ,PricePlan,Feature

class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')

class CertificateTranslation(TranslationOptions):
    fields = ('title','description')

class FeedBackTranslation(TranslationOptions):
    fields = ('comment',)

class FAQTransaltion(TranslationOptions):
    fields = ('answer','question')

class PricePlanTranslation(TranslationOptions):
    fields = ('limit_date','limit_user','title')

class FeatureTranslation(TranslationOptions):
    fields = ('title',)


for a,b in [(Certificate,CertificateTranslation),(WhyUs, WhyUsTranslation),(FeedBack,FeedBackTranslation),(FAQ,FAQTransaltion),(PricePlan,PricePlanTranslation),(Feature,FeatureTranslation)]:
    translator.register(a,b)

