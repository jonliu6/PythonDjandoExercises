from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="book-home"),
    #path("<int:book_id>/", views.book_detail, name="book-detail"),
    path("<slug:slug>", views.book_detail, name="book-detail"),
]
