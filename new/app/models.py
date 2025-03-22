from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Qns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)