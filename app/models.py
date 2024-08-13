from django.db import models
from django.core import validators
# Create your models here.
class Student(models.Model):
    sid=models.IntegerField()
    sn=models.CharField(max_length=100,validators=[validators.MinLengthValidator(5)])
    sa=models.IntegerField()
    mob=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    