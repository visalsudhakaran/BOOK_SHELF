from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('<int:pk>', views.book_detail, name='book-detail'),
    path('create', views.book_create, name='book-create'),
    path('<int:pk>/edit',views.book_update, name='book-update')
]
