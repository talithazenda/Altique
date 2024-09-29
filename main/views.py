import datetime
from django.shortcuts import get_object_or_404, render, redirect, reverse
from main.forms import ItemBarangForm
from main.models import ItemBarang
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    items = ItemBarang.objects.filter(user=request.user)
    # Ambil cookie dengan nilai default jika tidak ada
    last_login = request.COOKIES.get('last_login', 'Belum pernah login')  # Menambahkan default value

    context = {
        'nama_app': 'Altique!',
        'npm': '2306245554',
        'name': request.user.username,
        'class': 'PBP A',
        'items': items,
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
    data = ItemBarang.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemBarang.objects.all()
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
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item_barang(request, id):
    item = ItemBarang.objects.get(pk=id, user=request.user)
    if request.method == 'POST':
        form = ItemBarangForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('main:show_main')  # Redirect to main page after editing
    else:
        form = ItemBarangForm(instance=item)
    
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'edit_item_barang.html', context)

def delete_item_barang(request, id):
    item = get_object_or_404(ItemBarang, pk=id, user=request.user)
    item.delete()
    messages.success(request, "Item successfully deleted.")
    return redirect('main:show_main')  # Redirect to main page after deletion