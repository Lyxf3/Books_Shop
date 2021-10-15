from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from book import views as book_views

router = DefaultRouter()
router.register(r'book', book_views.BookViewSet, basename='book')
router.register(r'promo-code', book_views.PromoCodeViewSet, basename='promo-code')
router.register(r'author', book_views.AuthorViewSet, basename='author')
router.register(r'category', book_views.CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
]
