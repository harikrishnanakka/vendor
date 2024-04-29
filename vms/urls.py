from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', views.VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
    path('purchase_orders/', views.PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:vendor_id>/performance/', views.VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    
]
