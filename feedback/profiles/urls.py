from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("image_list", views.ViewProfileImagesView.as_view()),
]