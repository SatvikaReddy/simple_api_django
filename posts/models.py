from django.db import models
from django.db.models import TextField

# Create your models here.

class post(models.Model):
    userid=models.AutoField(primary_key=True)
    user=models.CharField(max_length=60)
    desc=models.CharField(max_length=60)

    def __str__(self):
        return self.user

class comment(models.Model):
    user = models.ForeignKey(post, on_delete=models.CASCADE)
    comment=TextField(max_length=500, blank=False)

    def __str__(self):
        return self.comment

