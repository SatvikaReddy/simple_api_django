from django.db import models

# Create your models here.

class post(models.Model):
    userid=models.AutoField(primary_key=True)
    user=models.CharField(max_length=60)
    desc=models.CharField(max_length=60)

    def __str__(self):
        return self.user