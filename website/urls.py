from django.conf.urls import url

from .views import *

# Application Routes (URLs)


app_name = "website"

urlpatterns = [
    # Home Page
    url(r"^$", ProductsPage.as_view(), name="products_page"),
    url(r"^checkout/$", CheckOutPage.as_view(), name="check_out_page"),
    url(r"^customer_info/$", CustomerInfo.as_view(), name="customer_info"),
    url(r"^pay_now/$", PayNowPage.as_view(), name="pay_now"),
    url(r"^thank_you/$", ThankYouPage.as_view(), name="thank_you"),
    url(r"^manage/$", AdminPage.as_view(), name="admin"),
    # Profile Page
    url(r"^profile$", ProfileView.as_view(), name="profile"),
]
