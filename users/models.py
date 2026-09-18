from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    display_name = models.CharField(max_length=100, blank=True)
    date_birth = models.DateField(blank=True, null=True)

    def  save(self, *args, **kwargs):
            if not self.display_name:
                self.display_name = self.username
            super().save(*args, **kwargs)