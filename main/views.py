from django.shortcuts import render
from .models import Product  # Import model Product

def home(request):
    context = {
        'app_name': 'Altique',
        'student_name': 'Talitha Zenda Shakira',
        'student_class': 'PBP A'
    }
    return render(request, 'home.html', context)


def product_list(request):
    products = Product.objects.all()  # Ambil semua produk
    context = {
        'products': products  # Kirim daftar produk ke template
    }
    return render(request, 'product_list.html', context)