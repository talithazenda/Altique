from django.shortcuts import render
from .models import Product  # Import model Product

from django.shortcuts import render

def show_main(request):
    context = {
        'nama_app' : 'Altique!',
        'npm' : '2306245554',
        'name': 'Talitha Zenda Shakira',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
