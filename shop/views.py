from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def category_list(request):
    categorii = Category.objects.all()
    return render(request, 'shop/index.html', {'categorii':categorii})