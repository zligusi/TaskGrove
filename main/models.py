from django.db import models
from django.utils.text import slugify

class Task(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='media/')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    ready = models.BooleanField(default=False)
    PRIORITY_ADD = [(0, 'none'), (1, 'low'), (2, 'medium'), (3, 'high'), (4, 'urgent')]
    priority = models.CharField(max_length=10, choices=PRIORITY_ADD, default=0)

    def  save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)