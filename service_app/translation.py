from modeltranslation.translator import TranslationOptions, translator
from .models import ServiceDescription, Service,Tag


class ServiceTranslation(TranslationOptions):
    fields = ('title',)


class ServiceDescriptionTranslation(TranslationOptions):
    fields = ('title','description')

class TagTranslation(TranslationOptions):
    fields = ('title',)

translator.register(ServiceDescription, ServiceDescriptionTranslation)
translator.register(Service, ServiceTranslation)
translator.register(Tag, TagTranslation)