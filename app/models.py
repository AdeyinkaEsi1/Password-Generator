from django.db import models
from django.contrib.auth.models import User


class GeneratedPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password: {self.password}, Created at: {self.created_at}"

