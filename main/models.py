from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Nama produk, dengan panjang maksimal 100 karakter
    price = models.IntegerField()  # Harga produk, menggunakan tipe integer
    description = models.TextField()  # Deskripsi produk, tipe teks untuk deskripsi panjang

    def __str__(self):
        return self.name  # Mengembalikan nama produk sebagai representasi string
