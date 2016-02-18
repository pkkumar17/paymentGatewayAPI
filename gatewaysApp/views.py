from django.shortcuts import render
import braintree
from django.http.response import HttpResponse
import json
from gatewaysApp.models import PaymentGateways
from rest_framework.decorators import api_view
from gatewaysApp.serializers import PaymentGatewaysSerializer
from rest_framework.response import Response


def index(request):
    return render(request, "gatewaysApp/index.html")

@api_view(['GET'])
def gatewaysList(request):
#     if request.method == "GET":
#         gateways = PaymentGateways.objects.all()      
    if request.method == 'GET':
        gateways = PaymentGateways.objects.all()
        serializer = PaymentGatewaysSerializer(gateways, many=True)
        return Response(serializer.data)
    
def getToken(request):
    
#   customer_id = request.POST.get('customer_id', '')
#   customer_id = "fd2v65k2m8msjx9p"
#   client_token = braintree.ClientToken.generate({
#     "customer_id": customer_id
#     })

    token = {"client_token":"d672866ab0dc761109aed6a10de96be5"}
    return HttpResponse(json.dumps(token))

def gatewaysSelection(request):
    if request.method == "POST":
        braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="fd2v65k2m8msjx9p",
                                  public_key="f63vkq5v5kgwjctn",
                                  private_key="d672866ab0dc761109aed6a10de96be5")
        
#        amount = request.POST.get("amount", '')
        nonce =request.POST.get('payment_method_nonce','')
    
        # Use payment method nonce here...
        result = braintree.Transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce
        })
        return render(request, "gatewaysApp/success.html") 
    
    else:
        pass


