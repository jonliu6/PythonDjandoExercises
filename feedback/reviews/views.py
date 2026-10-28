from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
# from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .models import Review

# Create your views here.
# using CreateView does not require FormView, as it is a subclass of FormView and provides additional functionality for creating objects. It automatically handles form validation, saving the object to the database, and redirecting to a success URL upon successful submission.
class ReviewView(CreateView):
    template_name = "reviews/review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/hello"

    def form_valid(self, form):
        form.save()  # Save the modelform data to the database
        self.success_url = self.success_url + f"?username={form.cleaned_data['user_name']}"
        return super().form_valid(form)

# class ReviewView(FormView):
#     template_name = "reviews/review.html"
#     form_class = ReviewForm
#     success_url = "/hello"

#     def form_valid(self, form):
#         form.save()  # Save the modelform data to the database
#         # return HttpResponseRedirect(f"/hello/?username={form.cleaned_data['user_name']}")
#         self.success_url = self.success_url + f"?username={form.cleaned_data['user_name']}"
#         return super().form_valid(form)

# class ReviewView(View):
#     # define HTTP methods (GET, POST, etc.) as methods of the class
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form": form})

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the modelform data to the database
#             return HttpResponseRedirect(f"/hello/?username={form.cleaned_data['user_name']}")
#         return render(request, "reviews/review.html", {"form": form})

# migrate the view method to a class-based view above
# def review(request):
#     # if request.method == "POST":
#     #     givenname = request.POST.get("username")
#     #     if givenname == "":
#     #         return render(request, "reviews/review.html", {"has_error": True})
#     #     return HttpResponseRedirect(f"/hello/?username={givenname}")
#     # elif request.method == "GET":
#     #     return render(request, "reviews/review.html", {"has_error": False})
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         # existing_review = Review.objects.filter(user_name=request.POST.get("user_name")).first()
#         # form = ReviewForm(request.POST, instance=existing_review) if existing_review else ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"]
#             # )
#             # review.save()
#             form.save()  # Save the modelform data to the database
#             # givenname = form.cleaned_data["user_name"]
#             # return HttpResponseRedirect(f"/hello/?username={review.user_name}")
#             return HttpResponseRedirect(f"/hello/?username={form.cleaned_data['user_name']}")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {"form": form})

# class HelloView(View):
#     def get(self, request):
#         givenname = request.GET.get("username")
#         return render(request, "reviews/hello.html", {"username": givenname})

class HelloView(TemplateView):
    template_name = "reviews/hello.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.GET.get("username")
        return context

# def hello(request):
#     givenname = request.GET.get("username")
#     return render(request, "reviews/hello.html", {"username": givenname})

# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["reviews"] = Review.objects.all()
#         return context
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews" # default is object_list, but we can change it to reviews for clarity

    # def get_queryset(self):
    #     base_queryset = super().get_queryset()
    #     # filter the queryset based on the query parameter "rating"
    #     data = base_queryset.filter(rating__gte=5) # filter reviews with rating greater than or equal to 4
    #     return data

# class ReviewDetailView(TemplateView):
#     template_name = "reviews/review_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = self.kwargs.get("pk")
#         context["review"] = Review.objects.get(pk=review_id)
#         return context

class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
    # Django automatically use the name of the model in lowercase as the context variable name, which is "review" in this case. We can also explicitly set it using context_object_name.
    context_object_name = "review" # default is object, but we can change it to review for clarity