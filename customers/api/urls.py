
from django.urls import path
from customers.api.views import CustomerAPIView, CustomerPassportAPIView, CustomersAPIView, PassportAPIView, PassportsAPIView


app_name = "customers_api"


urlpatterns = [
    path("customers/", CustomersAPIView.as_view(), name="customers"),
    path("customers/<int:pk>", CustomerAPIView.as_view(), name="customer"),
    path("passports/", PassportsAPIView.as_view(), name="passports"),
    path("passports/<int:pk>", PassportAPIView.as_view(), name="passport"),
    path("customer-passport/", CustomerPassportAPIView.as_view(), name="customer-passport"),
]