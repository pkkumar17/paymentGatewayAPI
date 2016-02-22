from django.shortcuts import render
import braintree
from django.http.response import HttpResponse
import json
from gatewaysApp.models import PaymentGateways
from rest_framework.decorators import api_view
from gatewaysApp.serializers import PaymentGatewaysSerializer
from rest_framework.response import Response


def index(request):
    return render(request, "index.html")

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

    token = {"client_token":"eyJ2ZXJzaW9uIjoyLCJhdXRob3JpemF0aW9uRmluZ2VycHJpbnQiOiIyZjJjZGFjMzEyZWMwZTYxYzk2ZDQ5M2JmOTk4N2E0MDZiNjQwZjVlZTc1ZmIwNzc3NzE3OTJiNzMwZjZhNzM1fGNyZWF0ZWRfYXQ9MjAxNi0wMi0yMlQwNTo1MzozOC4yOTM0MjA2MDQrMDAwMFx1MDAyNm1lcmNoYW50X2lkPTM0OHBrOWNnZjNiZ3l3MmJcdTAwMjZwdWJsaWNfa2V5PTJuMjQ3ZHY4OWJxOXZtcHIiLCJjb25maWdVcmwiOiJodHRwczovL2FwaS5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tOjQ0My9tZXJjaGFudHMvMzQ4cGs5Y2dmM2JneXcyYi9jbGllbnRfYXBpL3YxL2NvbmZpZ3VyYXRpb24iLCJjaGFsbGVuZ2VzIjpbXSwiZW52aXJvbm1lbnQiOiJzYW5kYm94IiwiY2xpZW50QXBpVXJsIjoiaHR0cHM6Ly9hcGkuc2FuZGJveC5icmFpbnRyZWVnYXRld2F5LmNvbTo0NDMvbWVyY2hhbnRzLzM0OHBrOWNnZjNiZ3l3MmIvY2xpZW50X2FwaSIsImFzc2V0c1VybCI6Imh0dHBzOi8vYXNzZXRzLmJyYWludHJlZWdhdGV3YXkuY29tIiwiYXV0aFVybCI6Imh0dHBzOi8vYXV0aC52ZW5tby5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tIiwiYW5hbHl0aWNzIjp7InVybCI6Imh0dHBzOi8vY2xpZW50LWFuYWx5dGljcy5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tIn0sInRocmVlRFNlY3VyZUVuYWJsZWQiOnRydWUsInRocmVlRFNlY3VyZSI6eyJsb29rdXBVcmwiOiJodHRwczovL2FwaS5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tOjQ0My9tZXJjaGFudHMvMzQ4cGs5Y2dmM2JneXcyYi90aHJlZV9kX3NlY3VyZS9sb29rdXAifSwicGF5cGFsRW5hYmxlZCI6dHJ1ZSwicGF5cGFsIjp7ImRpc3BsYXlOYW1lIjoiQWNtZSBXaWRnZXRzLCBMdGQuIChTYW5kYm94KSIsImNsaWVudElkIjpudWxsLCJwcml2YWN5VXJsIjoiaHR0cDovL2V4YW1wbGUuY29tL3BwIiwidXNlckFncmVlbWVudFVybCI6Imh0dHA6Ly9leGFtcGxlLmNvbS90b3MiLCJiYXNlVXJsIjoiaHR0cHM6Ly9hc3NldHMuYnJhaW50cmVlZ2F0ZXdheS5jb20iLCJhc3NldHNVcmwiOiJodHRwczovL2NoZWNrb3V0LnBheXBhbC5jb20iLCJkaXJlY3RCYXNlVXJsIjpudWxsLCJhbGxvd0h0dHAiOnRydWUsImVudmlyb25tZW50Tm9OZXR3b3JrIjp0cnVlLCJlbnZpcm9ubWVudCI6Im9mZmxpbmUiLCJ1bnZldHRlZE1lcmNoYW50IjpmYWxzZSwiYnJhaW50cmVlQ2xpZW50SWQiOiJtYXN0ZXJjbGllbnQzIiwiYmlsbGluZ0FncmVlbWVudHNFbmFibGVkIjp0cnVlLCJtZXJjaGFudEFjY291bnRJZCI6ImFjbWV3aWRnZXRzbHRkc2FuZGJveCIsImN1cnJlbmN5SXNvQ29kZSI6IlVTRCJ9LCJjb2luYmFzZUVuYWJsZWQiOmZhbHNlLCJtZXJjaGFudElkIjoiMzQ4cGs5Y2dmM2JneXcyYiIsInZlbm1vIjoib2ZmIn0"}
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
        return render(request, "success.html") 
    
    else:
        pass


