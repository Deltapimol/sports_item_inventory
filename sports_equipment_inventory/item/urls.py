from django.urls import path, include
from .views import ItemAPIView

urlpatterns = [
    path('items', ItemAPIView.as_view(), name='items-create-fetch'),
    path('items/<int:pk>', ItemAPIView.as_view(), name='item-update')
]
