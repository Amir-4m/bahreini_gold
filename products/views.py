from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductList(ListView):
    model = Product
    paginate_by = 50
    template_name = 'products/product-list.html'
