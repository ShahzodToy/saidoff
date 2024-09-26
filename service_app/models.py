from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(max_length=125)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.title
    

class ServiceDescription(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='descriptions')  
    image = models.ImageField(upload_to='service_desc')
    title = models.CharField(max_length=125)
    description = models.TextField()
    class Meta:
        verbose_name = _('ServiceDescription')
        verbose_name_plural = _('ServiceDescriptions')

    def __str__(self):
        return self.service.title
    

class Order(models.Model):
    name = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=125)
    service_name= models.ForeignKey(Service,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_checked = models.BooleanField(default=False)
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio')
    url_link = models.URLField()
    service_name = models.ForeignKey(Service,on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')

    def __str__(self):
        return f'Project for {self.service_name.title}'
    

class Tag(models.Model):
    title = models.CharField(max_length=125)
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.title

 
    
    
