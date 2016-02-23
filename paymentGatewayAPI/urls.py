"""paymentGatewayAPI URL Configuration"""


from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from gatewaysApp.views import index, getToken, gatewaysList, gatewaysSelection,\
    customerRegistration

urlpatterns = [
    url('^$', index, name = 'index'),
    url('^gatewaysList/$', gatewaysList, name = 'gatewaysList'),
    url('^checkout/$', gatewaysSelection, name = 'gatewaysSelection'),
    url('^getToken/', getToken, name = 'getToken'),
    url('^registration/$', customerRegistration, name = 'customerRegistration'),
    url(r'^admin/', include(admin.site.urls)),
]

