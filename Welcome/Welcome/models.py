from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    bio = models.TextField(max_length=1000)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username