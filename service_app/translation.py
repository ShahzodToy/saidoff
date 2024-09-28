from modeltranslation.translator import TranslationOptions, translator
from .models import ServiceDescription, Service,Tag, CategoryService


class ServiceTranslation(TranslationOptions):
    fields = ('title',)


class ServiceCategory(TranslationOptions):
    fields = ('title',)


class ServiceDescriptionTranslation(TranslationOptions):
    fields = ('title','description')


class TagTranslation(TranslationOptions):
    fields = ('title',)

translator.register(ServiceDescription, ServiceDescriptionTranslation)
translator.register(CategoryService,ServiceCategory)
translator.register(Service, ServiceTranslation)
translator.register(Tag, TagTranslation)