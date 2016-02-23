from django.contrib import admin
from django.db import models
from gatewaysApp.models import PaymentGateways, CustomerDetails


class PaymentGatewaysAdmin(admin.ModelAdmin):
    pass

class CustomerDetailsAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(PaymentGateways, PaymentGatewaysAdmin)
admin.site.register(CustomerDetails, CustomerDetailsAdmin)