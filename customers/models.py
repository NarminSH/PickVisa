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
    # relation
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, db_index=True, related_name="passports"
    )

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    scan_file = models.ImageField(upload_to='passport_images/')
    document_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    birth_date = models.DateField()
    personal_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES )
    issue_date = models.DateField()
    expire_date = models.DateField()
    issuing_authority = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.first_name