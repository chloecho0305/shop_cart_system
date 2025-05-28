from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'frontend/home.html')
def product_list(request):
    return render(request, 'frontend/products.html')