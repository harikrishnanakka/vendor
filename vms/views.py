from django.shortcuts import render
from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from django.db.models import Count, Avg
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, Avg
from rest_framework.permissions import IsAuthenticated

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]


class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


def calculate_vendor_performance(vendor):
    # On-Time Delivery Rate
    completed_orders_count = vendor.purchaseorder_set.filter(status='completed').count()
    on_time_delivery_count = vendor.purchaseorder_set.filter(status='completed', delivery_date__lte=timezone.now()).count()
    vendor.on_time_delivery_rate = on_time_delivery_count / completed_orders_count if completed_orders_count != 0 else 0
    
    # Quality Rating Average
    vendor.quality_rating_avg = vendor.purchaseorder_set.filter(status='completed').aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0
    
    # Average Response Time
    avg_response_time = vendor.purchaseorder_set.filter(
        status='completed', 
        acknowledgment_date__isnull=False
    ).aggregate(
        avg_response=Avg(F('acknowledgment_date') - F('issue_date'))
    )['avg_response']

    if avg_response_time is not None:
        vendor.average_response_time = avg_response_time.total_seconds() / 3600
    else:
        vendor.average_response_time = 0
    
    # Fulfilment Rate
    total_orders_count = vendor.purchaseorder_set.count()
    fulfilled_orders_count = vendor.purchaseorder_set.filter(status='completed').count()
    vendor.fulfillment_rate = fulfilled_orders_count / total_orders_count if total_orders_count != 0 else 0
    
    # Save the vendor object with updated performance metrics
    vendor.save()

     
    
class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Calculate performance metrics
        calculate_vendor_performance(vendor)
        
        # Prepare response data
        performance_data = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate
        }
        
        return Response(performance_data, status=status.HTTP_200_OK)
    