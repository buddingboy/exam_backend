from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    highest_qualification = models.CharField(max_length=100, null=True, blank=True)
    purpose = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    relationship_status = models.CharField(max_length=50, null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    credit_point = models.IntegerField(null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    login_streak = models.IntegerField(null=True, blank=True)
    last_ip_address = models.GenericIPAddressField(null=True, blank=True)
    otp_attempts = models.IntegerField(null=True, blank=True)
    email_attempts = models.IntegerField(null=True, blank=True)