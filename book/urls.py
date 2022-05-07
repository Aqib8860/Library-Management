from django.urls import path, include
from rest_framework import routers
from book import views


router = routers.DefaultRouter()
router.register('book', views.BookViewSet, basename='viewaddbook')
router.register('list-book', views.ListBookViewSet, basename='listbook')
router.register('borrow-book', views.BorrowedViewSet, basename='borrowbook')
router.register('return-book', views.ReturnViewSet, basename='returnbook')


urlpatterns = [
    path('', include(router.urls)),
]
