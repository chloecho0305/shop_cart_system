from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@staff_member_required
def dashboard(request):
    return render(request, 'backend/dashboard.html')

@staff_member_required
def manage_products(request):
    return render(request, 'backend/manage_products.html')