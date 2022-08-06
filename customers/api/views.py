from django.http import JsonResponse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView
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


class CustomerPassportsAPIView(ListAPIView):
    queryset = Passport.objects.all()
    serializer_class = PassportListSerializer

    def get(self, *args, **kwargs):
        current_customer = Customer.objects.filter(id=kwargs.get("pk")).first()
        passports = Passport.objects.filter(customer=current_customer)
        if not passports:
            return JsonResponse(data=[], status=200, safe=False)
        print(passports)
        serializer = PassportListSerializer(
            passports, many=True, context={"request": self.request}
        )
        return JsonResponse(data=serializer.data, safe=False)

