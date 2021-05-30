from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


        




