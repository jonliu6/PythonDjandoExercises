from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView #  TemplateView, DetailView, FormView, UpdateView, DeleteView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.
def store_profile(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ViewProfileImagesView(ListView):
    model = UserProfile
    template_name = "profiles/view_profile_images.html"
    context_object_name = "profiles"

# class CreateProfileView(View): # replaced by above CreateView, no need to forms.py
#     def get(self, request):
#         return render(request, "profiles/create_profile.html", {
#             "form": ProfileForm()
#             })
#     def post(self, request):
#         # store_profile(request.FILES["imgFile"]) # imgFile is the name of the input field in the form, but we changed it to profileImg in the form class, so we need to use that name instead.
#         # print(request.FILES["imgFile"])
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             # store_profile(request.FILES["profileImg"])
#             profile = UserProfile(proflie_image=request.FILES["profileImg"]) # profileImg is the name of the input field in the form, but we changed it to profileImg in the form class, so we need to use that name instead.
#             profile.save() # save the profile (path) to the database
#             return HttpResponseRedirect("/profiles")

#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })
