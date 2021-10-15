from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from purchase import views as purchase_views

router = DefaultRouter()
router.register(r'purchase', purchase_views.PurchaseViewSet, basename='purchase')

urlpatterns = [
    path('', include(router.urls)),
]
