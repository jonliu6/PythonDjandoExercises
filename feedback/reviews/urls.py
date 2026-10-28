from django.urls import path
from . import views
urlpatterns = [
    # path("", views.review),
    # use the class-based view instead of the function-based view above
    path("", views.ReviewView.as_view()),
    #path("hello/", views.hello)
    path("hello/", views.HelloView.as_view()),
    path("reviews/", views.ReviewListView.as_view(), name="review_list"),
    path("reviews/<int:pk>/", views.ReviewDetailView.as_view(), name="review_detail"),
]
