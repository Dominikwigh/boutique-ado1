from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Mj13VLnd1MBA1Tnc6turCAmGCzANesZFOKppw5UuiisV6ZCjV35ZpO4hdD3CwplqcP5bog8oc7W1qszOlad6m9m00vk6sy4Gi'
    }

    return render(request, template, context)