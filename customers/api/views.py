from contractsPY import if_fails, Usecase
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

from scan_file import send_passport


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


    def post(self, *args, **kwargs):
        cart_data = self.request.data
        serializer = PassportSerializer(data=cart_data, context={
            'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        image = cart_data["scan_file"]
        send_passport.apply(image=f'passport_images/{image}')
        return JsonResponse(data=serializer.data, safe=False, status=201)


class PassportAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PassportSerializer
    queryset = Passport.objects.all()
    lookup_url_kwarg = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PassportListSerializer
        return super(PassportAPIView, self).get_serializer_class()


class UnitedCustomerPassportAPIView(CreateAPIView):
    serializer_class = CustomerPassportSerializer
    queryset = Customer.objects.all()


class CustomerPassportsAPIView(ListAPIView):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer

    def get(self, *args, **kwargs):
        current_customer = Customer.objects.filter(id=kwargs.get("pk")).first()
        passports = Passport.objects.filter(customer=current_customer)
        if not passports:
            return JsonResponse(data=[], status=200, safe=False)
        serializer = PassportSerializer(
            passports, many=True, context={"request": self.request}
        )
        return JsonResponse(data=serializer.data, safe=False)
