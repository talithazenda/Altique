import uuid
from django.db import models

class ItemBarang(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Add this line
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    waktu_buat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

