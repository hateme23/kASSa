from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Имя товара',
            'price': 'Цена',
            'description': 'Описание',
            'discount': 'Скидка',
            'purchase_price': 'Цена закупки',
            'supplier': 'Поставщик',
            'category': 'Категория товара',
            'quantity': 'Количество'
        }