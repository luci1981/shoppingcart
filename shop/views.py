from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def category_list(request):
    categorii = Category.objects.all()
    return render(request, 'shop/index.html', {'categorii':categorii})

def product_list(request, pk):
    categorii = Category.objects.all()
    produse = get_object_or_404(Category, pk=pk)
    context = {'produse': produse, 'categorii':categorii}
    return render(request, 'shop/product_list.html', context)
