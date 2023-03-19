from django.urls import path
from product import views

urlpatterns = [
    path('browse/', views.ProductBrowseView.as_view(), name='browse'),
    path('detail/', views.ProductDetailView.as_view(), name='detail')
]