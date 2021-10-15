from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from user import views as user_views

router = DefaultRouter()
router.register(r'user', user_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
