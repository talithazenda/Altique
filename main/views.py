from django.http import JsonResponse
from .models import ItemBarang
import datetime
import json
from django.shortcuts import get_object_or_404, render, redirect, reverse
from main.forms import ItemBarangForm
from main.models import ItemBarang
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.utils.html import strip_tags
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout

@login_required(login_url='/login')
def show_main(request):
    # Ambil cookie dengan nilai default jika tidak ada
    last_login = request.COOKIES.get('last_login', str(datetime.datetime.now()))  # Menambahkan default value

    context = {
        'nama_app': 'Altique!',
        'npm': '2306245554',
        'name': request.user.username,
        'class': 'PBP A',
        'last_login': last_login,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login/')  # Redirect ke login jika pengguna tidak terautentikasi
def show_items(request):
    items = ItemBarang.objects.filter(user=request.user)
    context = {
        'items': items,
    }
    return render(request, 'item_list.html', context)

# views.py
def add_item_barang(request):
    form = ItemBarangForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        item_barang = form.save(commit=False)
        item_barang.user = request.user  # Associate the item with the current user
        item_barang.save()
        return redirect('main:show_main')  # Redirect to main page after adding
    context = {'form': form}
    return render(request, 'add_item_barang.html', context)

def show_xml(request):
    data = ItemBarang.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemBarang.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemBarang.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemBarang.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        if password1 != password2:
            return JsonResponse({"status": False, "message": "Passwords do not match."}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": False, "message": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, password=password1)
        user.save()

        return JsonResponse({"username": user.username, "status": 'success', "message": "User created successfully!"}, status=200)

    return JsonResponse({"status": False, "message": "Invalid request method."}, status=400)

from django.contrib.auth import authenticate, login as auth_login

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({"username": user.username, "status": True, "message": "Login sukses!"}, status=200)
            return JsonResponse({"status": False, "message": "Akun dinonaktifkan."}, status=401)

        return JsonResponse({"status": False, "message": "Login gagal, periksa kembali email atau kata sandi."}, status=401)

    return JsonResponse({"status": False, "message": "Invalid request method."}, status=400)

@csrf_exempt
def logout(request):
    try:
        username = request.user.username
        auth_logout(request)
        return JsonResponse({"username": username, "status": True, "message": "Logout berhasil!"}, status=200)
    except:
        return JsonResponse({"status": False, "message": "Logout gagal."}, status=401)


@csrf_exempt
@login_required(login_url='/login/')
def edit_item_barang(request, id):
    try:
        item = ItemBarang.objects.get(pk=id, user=request.user)
        if request.method == 'POST':
            data = json.loads(request.body)
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            item.price = data.get('price', item.price)
            item.stock = data.get('stock', item.stock)
            item.save()

            return JsonResponse({'status': 'success', 'message': 'Item updated successfully!'})
    except ItemBarang.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Item not found!'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def delete_item_barang(request, id):
    try:
        item = ItemBarang.objects.get(pk=id, user=request.user)
        if request.method == 'POST':
            item.delete()
            return JsonResponse({'status': 'success', 'message': 'Item deleted successfully!'})
    except ItemBarang.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Item not found!'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

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
