import uuid  # Tambahkan ini untuk menggunakan UUID
from django.db import models
from django.contrib.auth.models import User

class ItemBarang(models.Model):
    CATEGORY_CHOICES = [
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('aksesoris', 'Aksesoris'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID field
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.name
