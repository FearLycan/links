from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    link = models.CharField(max_length=250)
    hash = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=300, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link
