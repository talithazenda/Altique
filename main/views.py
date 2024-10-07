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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm(request)
    
    csrf_token = get_token(request)  # Get CSRF token from request
    print("CSRF Token:", csrf_token)  # Log CSRF token to console for debugging
    
    context = {'form': form, 'csrf_token': csrf_token}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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
