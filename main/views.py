from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.middleware.csrf import get_token
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST
from .models import ItemBarang
from .forms import ItemBarangForm
import json
import datetime
from django.utils.html import strip_tags
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


@login_required(login_url='/login/')
def show_main(request):
    last_login = request.COOKIES.get('last_login', str(datetime.datetime.now()))
    context = {
        'nama_app': 'Altique!',
        'npm': '2306245554',
        'name': request.user.username,
        'class': 'PBP A',
        'last_login': last_login,
    }
    return render(request, 'main.html', context)


@login_required(login_url='/login/')
def show_items(request):
    items = ItemBarang.objects.filter(user=request.user)
    context = {'items': items}
    return render(request, 'item_list.html', context)


def show_xml(request):
    data = ItemBarang.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = ItemBarang.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = get_object_or_404(ItemBarang, pk=id)
    return JsonResponse(serializers.serialize("json", [data]), safe=False)

def show_xml_by_id(request, id):
    data = ItemBarang.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


@csrf_exempt
@require_POST
def register(request):
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        password1 = data.get('password1', '')
        password2 = data.get('password2', '')

        if password1 != password2:
            return JsonResponse({"status": False, "message": "Passwords do not match."}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": False, "message": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, password=password1)
        return JsonResponse({"username": user.username, "status": "success", "message": "User created successfully!"}, status=200)
    except Exception as e:
        return JsonResponse({"status": False, "message": str(e)}, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'csrf_token': get_token(request)})


def logout_user(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('/login/')


@login_required(login_url='/login/')
@require_POST
def add_item_barang(request):
    form = ItemBarangForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return redirect('main:show_main')
    return render(request, 'add_item_barang.html', {'form': form})


@login_required(login_url='/login/')
@require_http_methods(["GET", "POST"])
def edit_item_barang(request, id):
    item = get_object_or_404(ItemBarang, pk=id, user=request.user)
    if request.method == 'POST':
        form = ItemBarangForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Item updated successfully!"})
        return JsonResponse({"status": "error", "message": "Invalid data!"}, status=400)
    return render(request, 'edit_item_barang.html', {'item': item})


@login_required(login_url='/login/')
@require_POST
def delete_item_barang(request, id):
    item = get_object_or_404(ItemBarang, pk=id, user=request.user)
    item.delete()
    return JsonResponse({"status": "success", "message": "Item deleted successfully!"})


@csrf_exempt
@require_http_methods(["GET", "POST"])
def add_item_barang_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validasi dan proses data di sini
            name = strip_tags(data.get('name', '').strip())
            description = strip_tags(data.get('description', ''))
            price = data.get('price', 0)
            stock = data.get('stock', 0)
            category = data.get('category', 'baju')

            if not name:
                name = 'My Items'  # Default if name is blank

            new_item = ItemBarang.objects.create(
                name=name,
                description=description,
                price=price,
                stock=stock,
                category=category,
                user=request.user
            )
            new_item.save()
            return JsonResponse({'status': 'success', 'message': 'Item added!'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return render(request, 'add_item_barang_ajax.html')

def items_list(request):
    items = ItemBarang.objects.all().values()
    items_list = list(items)
    return JsonResponse(items_list, safe=False)

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        try:
            # Mengubah request body dari JSON menjadi dictionary
            data = json.loads(request.body)
            # Periksa apakah data yang dibutuhkan ada, jika tidak, kembalikan respons error
            if 'name' not in data or 'description' not in data or 'price' not in data or 'stock' not in data or 'category' not in data:
                return JsonResponse({"status": "error", "message": "Data yang dibutuhkan tidak lengkap."}, status=400)

            # Membuat instance ItemBarang menggunakan data dari Flutter
            new_item = ItemBarang.objects.create(
                name=data["name"],  # Ambil langsung dari data tanpa default
                description=data["description"],  # Ambil langsung dari data tanpa default
                price=int(data["price"]),  # Ambil langsung dari data tanpa default
                stock=int(data["stock"]),  # Ambil langsung dari data tanpa default
                category=data["category"] , # Ambil langsung dari data tanpa default
                user=request.user

            )
            # Menyimpan instance baru ke database
            new_item.save()

            # Mengirim respons sukses ke aplikasi Flutter
            return JsonResponse({"status": "success", "message": "Item berhasil dibuat!"}, status=200)
        
        except Exception as e:
            # Mengirim respons error jika terjadi kesalahan saat menyimpan data
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    
    # Mengirim respons error jika request method bukan POST
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)