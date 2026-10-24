from django.urls import path
from . import views
urlpatterns = [
    # path("", views.review),
    # use the class-based view instead of the function-based view above
    path("", views.ReviewView.as_view()),
    path("hello/", views.hello)
]
