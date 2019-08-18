from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import View

from django.shortcuts import render

from .models import Product

# Application Views


# Template Views
class ProductsPage(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        context = {
            'products': Product.objects.all()
        }
        return render(self.request, "website/products_page.html", context)


class CheckOutPage(LoginRequiredMixin, TemplateView):
    template_name = 'website/check_out.html'


class CustomerInfo(LoginRequiredMixin, TemplateView):
    template_name = 'website/customer_info.html'


class PayNowPage(LoginRequiredMixin, TemplateView):
    template_name = 'website/pay_now.html'


class ThankYouPage(LoginRequiredMixin, TemplateView):
    template_name = 'website/thanks.html'


class AdminPage(LoginRequiredMixin, TemplateView):
    template_name = 'website/admin.html'

# Create Views
# Update Views
# Delete Views
# Misc Views
