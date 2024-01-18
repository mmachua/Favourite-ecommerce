from django.shortcuts import render ,redirect
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import OrderItem ,Order
from orders.forms import OrderCreateForm
from cart.cart import Cart 
from django.urls import reverse
#from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    order = Order(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            phone_no = form.cleaned_data['phone_no']
            city = form.cleaned_data['city']
            
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order = order,
                    product = item['product'],
                    price = item['price'],
                    quantity = item['quantity']
                )
            cart.clear()
            order : Order(request)
            #launch assy. tasks
            #order_created.delay(order.id)
            #set the order in the session  
            request.session['order_id'] = order.id
            #redirect to payment
            return redirect(reverse('payment:process'))
        
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})
