from django.contrib import admin
from .models import WhyUs, Partners, Certificate, Subscribe, FAQ, FAQCategory, Team, FeedBack,PricePlan,Feature
from modeltranslation.admin import TranslationAdmin


class WhyUsTranslationAdmin(TranslationAdmin):
    list_display = ('title', 'description')

admin.site.register(WhyUs, WhyUsTranslationAdmin)


for a in [Partners, Certificate, Subscribe, FAQ, FAQCategory, Team, FeedBack,PricePlan,Feature]:
    admin.site.register(a)

    
