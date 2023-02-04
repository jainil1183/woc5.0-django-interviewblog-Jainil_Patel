from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200,null=True)
    program = models.CharField(max_length=200,null=True)
    graduation_year = models.IntegerField(null=True)

    def __str__(self):
        return self.username.first_name