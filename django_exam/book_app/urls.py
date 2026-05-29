from django.urls import path

from . import views


urlpatterns = [

    path('', views.book_list),

    path('add/', views.book_add),

    path('edit/<int:id>/', views.book_edit),

    path('delete/<int:id>/', views.book_delete),
]
