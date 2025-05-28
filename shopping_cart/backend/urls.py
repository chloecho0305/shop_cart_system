from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard, name='admin_dashboard'),
    path('product/',views.manage_products, name='manage_products'),
]