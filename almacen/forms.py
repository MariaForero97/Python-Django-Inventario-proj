from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','sku','description','quantity','price']
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
        }
