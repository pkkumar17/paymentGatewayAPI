from django.db import models

class PaymentGateways(models.Model):
    gateway_name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.gateway_name
    