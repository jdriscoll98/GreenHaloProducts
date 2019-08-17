from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

# Application Views


# Template Views
class ProductsPage(LoginRequiredMixin, TemplateView):
    template_name = "website/products_page.html"


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
