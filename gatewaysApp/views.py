from django.shortcuts import render
import braintree
from django.http.response import HttpResponse
import json
from gatewaysApp.models import PaymentGateways, CustomerDetails
from rest_framework.decorators import api_view
from gatewaysApp.serializers import PaymentGatewaysSerializer
from rest_framework.response import Response

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="fd2v65k2m8msjx9p",
                                  public_key="f63vkq5v5kgwjctn",
                                  private_key="d672866ab0dc761109aed6a10de96be5")

def index(request):
    return render(request, "index.html")

@api_view(['GET'])
def gatewaysList(request):
    if request.method == 'GET':
        gateways = PaymentGateways.objects.all()
        serializer = PaymentGatewaysSerializer(gateways, many=True)
        return Response(serializer.data)

def customerRegistration(request):

    if request.Method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        company = request.POST.get("company", '')
        email = request.POST.get("email")
        phone = request.POST.get("phone", '312.555.1234')
        fax = request.POST.get("fax", '614.555.5678')
        website = request.POST.get("website", 'www.xavient.com')
#         
        customerData = {
                        "first_name":first_name,
                        "last_name":last_name,
                        "company":company,
                        "email":email,
                        "phone":phone,
                        "fax":fax,
                        "website":website
                        }

        result = braintree.Customer.create(customerData)
        if result.is_success:
            customer_id = result.customer.id
            customerDetails = CustomerDetails(
                                              first_name=first_name,
                                              last_name=last_name,
                                              customer_email=email,
                                              customer_id=customer_id,
                                              company=company,
                                              phone=phone,
                                              fax=fax,
                                              website=website
                                              )
        return render(request, "success.html")
    
def getToken(request):     
    
    customer = CustomerDetails.objects.get(customer_email="pkumar17@xavient.com")   
    if customer:
        customer_id = customer.customer_id
        client_token = braintree.ClientToken.generate({"customer_id": customer_id})
        
        client_token_dict = {"client_token":client_token}
        
        return HttpResponse(json.dumps(client_token_dict))
    else:
        return HttpResponse("%s is not available!!!" % (customer) )

def gatewaysSelection(request):
    if request.method == "POST":  
        nonce =request.POST.get('payment_method_nonce','')  
        if nonce:
            result = braintree.Transaction.sale({
                                                 "amount": "10.00",
                                                 "payment_method_nonce": nonce
                                                 })
            
            return render(request, "success.html") 
        
        else:
            return HttpResponse("Error: Payment Method Nonce is not available!!!")
    
    else:
        pass


