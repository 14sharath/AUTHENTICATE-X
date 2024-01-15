from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    firstname = models.CharField(max_length=100, default="")
    secondname = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    date = models.DateField(null=True, blank=True)  # Allow null and blank for date of birth
    # address = models.TextField(max_length=1000, default="")
    pincode=models.CharField(max_length=6,default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.firstname
    





