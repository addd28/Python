from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=200)

    price = models.FloatField()

    description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='books/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title