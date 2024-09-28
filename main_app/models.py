from django.db import models
from django.utils.translation import gettext_lazy as _

class WhyUs(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    image = models.ImageField(upload_to='whyus')

    class Meta:
        verbose_name = _('WhyUs')
        

    def __str__(self):
        return self.title
    
    

class Partners(models.Model):
    image = models.ImageField(upload_to='partners')

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
        
   
    def __str__(self):
        return self.image.name
    

class Team(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='team')
    profession = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self):
        return self.name
    
    
class Certificate(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(upload_to='subscribe')
    description  = models.TextField()
    class Meta:
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')
   

    def __str__(self):
        return self.title
    
class FeedBack(models.Model):
    name = models.CharField(max_length=125)
    comment = models.TextField()
    image = models.ImageField(upload_to='feedback')
    profession = models.CharField(max_length=125)
    class Meta:
        verbose_name = _('FeedBack')
        verbose_name_plural = _('FeedBacks')
    

    def __str__(self):
        return self.name
    

class FAQCategory(models.Model):
    title = models.CharField(max_length=125)
    class Meta:
        verbose_name = _('FAQCategory')
        verbose_name_plural = _('FAQCategorys')

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    faq_page = models.ForeignKey(FAQCategory,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.faq_page.title
    
class Feature(models.Model):
    title = models.CharField(max_length=125)
    tick = models.BooleanField(default=False)
    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.title


class PricePlan(models.Model):
    title = models.CharField(max_length=125)
    price = models.IntegerField()
    limit_date = models.CharField(max_length=125)
    limit_user = models.CharField(max_length=125)
    features = models.ManyToManyField(Feature)
    class Meta:
        verbose_name = _('PricePlan')
        verbose_name_plural = _('PricePlans')

    def __str__(self):
        return self.title




    


    







