from django.urls import path
from book.views import GetAllBooks, GetBook

urlpatterns = [
    path('<int:pk>/', GetAllBooks.as_view()),
    path('', GetBook.as_view()),
]
