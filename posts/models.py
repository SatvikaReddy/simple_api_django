from django.db import models
from django.db.models import TextField
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    userid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    desc=models.CharField(max_length=60)

    def __str__(self):
        return '{} by {}'.format(self.desc, self.user)

class comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    comment=TextField(max_length=500, blank=False)

    def __str__(self):
        return '{} by {}'.format(self.comment, self.user)

