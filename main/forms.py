from django import forms
from main.models import ItemBarang
from django.utils.html import strip_tags

CATEGORY_CHOICES = [
    ('baju', 'Baju'),
    ('celana', 'Celana'),
    ('aksesoris', 'Aksesoris'),
]

class ItemBarangForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = ItemBarang
        fields = ['name', 'description', 'price', 'stock', 'category']
        widgets = {
            'category': forms.RadioSelect(choices=CATEGORY_CHOICES),
        }

    def clean_name(self):
        name = strip_tags(self.cleaned_data.get('name', ''))
        if not name:
            raise forms.ValidationError("This field cannot be blank.")
        return name

    def clean_description(self):
        description = strip_tags(self.cleaned_data.get('description', ''))
        if not description:
            raise forms.ValidationError("This field cannot be blank.")
        return description
    
    def clean_price(self):
        price = strip_tags(self.cleaned_data.get('price', ''))
        if price is None or price == '':
            raise forms.ValidationError("This field cannot be blank")  # Custom error message
        return price

    def clean_stock(self):
        stock = strip_tags(self.cleaned_data.get('stock', ''))
        if stock is None or stock == '':
            raise forms.ValidationError("This field cannot be blank")  # Custom error message
        return stock

    def clean_category(self):
        category = strip_tags(self.cleaned_data.get('category', ''))
        if not category:
            raise forms.ValidationError("Please select a category")  # Custom error message
        return category
