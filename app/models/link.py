from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Link(models.Model):
    link = models.CharField(max_length=250)
    hash = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=300, null=True, default=None, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link

    def random_hash(self):
        while True:
            random_hash = get_random_string(length=5)
            obj = self.objects.get(hash=random_hash)

            if obj is None:
                break

        return random_hash
