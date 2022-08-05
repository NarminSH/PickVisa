from django.db import models



class Customer(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name


class Passport(models.Model):
    # relations
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, db_index=True, related_name="passports"
    )

    document_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    birth_date = models.CharField(max_length=20)
    personal_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    issue_date = models.CharField(max_length=20)
    expire_date = models.CharField(max_length=20)
    issuing_authority = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.first_name