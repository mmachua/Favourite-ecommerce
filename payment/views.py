from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import requests

access_token = "Access-Token"
api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode": " ",
    "ResponseType": " ",
    "ConfirmationURL": "http://ip_address:port/confirmation",
    "ValidationURL": "http://ip_address:port/validation_url"}

#response = requests.post(api_url, json = request, headers=headers)

#print (response.text)


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_process(request):
    
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECIEVER_EMAIL,
        'amount' : '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}' .format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_re_path': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_re_path': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_re_path': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', { 'order': order,
                                                    'form':form}) 