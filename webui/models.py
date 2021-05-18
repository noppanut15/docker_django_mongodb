from djongo import models

class Contacts(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)