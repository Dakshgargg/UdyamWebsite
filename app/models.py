from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator

class details(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    year = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\d{9,10}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list
    def __str__(self):
        return self.first_name