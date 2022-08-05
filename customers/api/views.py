from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from customers.api.serializers import (
    CustomerPassportSerializer, 
    CustomerSerializer, 
    PassportListSerializer, 
    PassportSerializer
)

from customers.models import Customer, Passport


class CustomersAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_url_kwarg = "pk"


class PassportsAPIView(ListCreateAPIView):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PassportListSerializer
        return super(PassportsAPIView, self).get_serializer_class()


class PassportAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PassportSerializer
    queryset = Passport.objects.all()
    lookup_url_kwarg = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PassportListSerializer
        return super(PassportAPIView, self).get_serializer_class()


class CustomerPassportAPIView(CreateAPIView):
    serializer_class = CustomerPassportSerializer
    queryset = Customer.objects.all()
