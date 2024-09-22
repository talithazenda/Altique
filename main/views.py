import datetime
from django.shortcuts import render, redirect
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
    context = {
        'nama_app': 'Altique!',
        'npm': '2306245554',
        'name': request.user.username,
        'class': 'PBP A',
        'items': items,
        'last_login': request.COOKIES['last_login'],
        
    }
    return render(request, 'main.html', context)

def show_items(request):
    items = ItemBarang.objects.filter(user=request.user)
    context = {
        'items': items,
    }
    return render(request, 'item_list.html', context)

def add_item_barang(request):
    form = ItemBarangForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        item_barang = form.save(commit=False)
        item_barang.user = request.user  # Set pengguna yang sedang login sebagai pengguna yang menciptakan item
        item_barang.save()
        return redirect('main:show_items')  # Arahkan ke show_items setelah menambah item
    
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