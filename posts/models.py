import django.utils.timezone
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
