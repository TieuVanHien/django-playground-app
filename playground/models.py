from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"