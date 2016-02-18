from django.contrib import admin
from django.db import models
from gatewaysApp.models import PaymentGateways


class PaymentGatewaysAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(PaymentGateways, PaymentGatewaysAdmin)