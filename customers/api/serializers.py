from rest_framework import serializers
from customers.models import Customer, Passport


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "name",
            "surname",
            "email",
            "phone",
            "created_at",
        )


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = (
            "id",
            "customer",
            "document_number",
            "first_name",
            "last_name",
            "patronymic",
            "nationality",
            "birth_date",
            "personal_number",
            "gender",
            "issue_date",
            "expire_date",
            "issuing_authority",
            "created_at",
        )


class PassportListSerializer(PassportSerializer):
    customer = CustomerSerializer()



class OnlyPassportSerializer(serializers.ModelSerializer): # this serializer is without customer field
    class Meta:
        model = Passport
        fields = (
            "id",
            "document_number",
            "first_name",
            "last_name",
            "patronymic",
            "nationality",
            "birth_date",
            "personal_number",
            "gender",
            "issue_date",
            "expire_date",
            "issuing_authority",
            "created_at",
        )


class CustomerPassportSerializer(serializers.ModelSerializer):
    passports = OnlyPassportSerializer(many=True)

    class Meta:
        model = Customer
        fields = (
            "id",
            "name",
            "surname",
            "email",
            "phone",
            "passports",
            "created_at",
        )

    def create(self, validated_data):
        passports_data = validated_data.pop('passports')
        customer = Customer.objects.create(**validated_data)
        for passport_data in passports_data:
            Passport.objects.create(customer=customer, **passport_data)
        return customer
