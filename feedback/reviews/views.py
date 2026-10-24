from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
# from .models import Review

# Create your views here.
class ReviewView(View):
    # define HTTP methods (GET, POST, etc.) as methods of the class
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save the modelform data to the database
            return HttpResponseRedirect(f"/hello/?username={form.cleaned_data['user_name']}")
        return render(request, "reviews/review.html", {"form": form})

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

def hello(request):
    givenname = request.GET.get("username")
    return render(request, "reviews/hello.html", {"username": givenname})