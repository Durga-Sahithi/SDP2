from django.db import models

# Create your models here.

class datetime1(models.Model):
    time12=models.TextField(max_length=255)
    class Meta:
        db_table="datetime1"

class Register(models.Model):
    username = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=122)
    mobileno = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    date = models.DateField()

    def _str_(self):
        return self.username


