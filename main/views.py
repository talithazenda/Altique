from django.shortcuts import render, redirect
from main.forms import ItemBarangForm
from main.models import ItemBarang
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    items = ItemBarang.objects.all()
    context = {
        'nama_app': 'Altique!',
        'npm': '2306245554',
        'name': 'Talitha Zenda Shakira',
        'class': 'PBP A',
        'items': items
    }
    return render(request, 'main.html', context)

def show_items(request):
    items = ItemBarang.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'item_list.html', context)

def add_item_barang(request):
    form = ItemBarangForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
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

