from django.shortcuts import render, get_object_or_404
from .models import Post

def get_date(post):
    return post["date"]

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]  # Order posts by date in descending order, and only get the first 3 posts
    #sorted_posts = sorted(all_posts, key=get_date)
    #latest_posts = sorted_posts[-3:]  # Get the last 3 posts
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by('-date')  # Order posts by date in descending order
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})

def post_detail(request, slug):
    found_post = get_object_or_404(Post, slug=slug)  # Get the post with the matching slug
    # found_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": found_post,
        "post_tags": found_post.tags.all()
    })