from django.db import models

class PaymentGateways(models.Model):
    gateway_name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.gateway_name
    
class CustomerDetails(models.Model):
    
    first_name = models.CharField(max_length=50, null = False)
    last_name = models.CharField(max_length=50, null = False)
    customer_email = models.EmailField(max_length=100, unique= True, null = False)
    customer_id = models.IntegerField(unique= True, null = False)
    company = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=25, default='')
    fax = models.CharField(max_length=25, default='')
    website = models.URLField(max_length=75, default='')
    
    def __str__(self):
        return self.first_name