from django.forms import ModelForm
from main.models import ItemBarang

class ItemBarangForm(ModelForm):
    class Meta:
        model = ItemBarang
        fields = ['name', 'description', 'price', 'stock']
