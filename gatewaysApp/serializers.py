from rest_framework import serializers
from gatewaysApp.models import PaymentGateways

class PaymentGatewaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentGateways
        fields = ('id', 'gateway_name',)