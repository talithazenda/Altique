from django import forms
from main.models import ItemBarang

class ItemBarangForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('aksesoris', 'Aksesoris'),
    ]
    
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = ItemBarang
        fields = ['name', 'description', 'price', 'stock', 'category']
        widgets = {
            'category': forms.RadioSelect(choices=ItemBarang.CATEGORY_CHOICES),
        }
