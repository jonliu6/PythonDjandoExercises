from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "first-post",
        "image": "wolf.jpeg",
        "author": "John Smith",
        "date": date(2026,9,20),
        "title": "A Running Wolf",
        "excerpt": "The wolf is running towards the camera.",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    },
    {
            "slug": "second-post",
            "image": "Grumpy Cat.jpg",
            "author": "Jane Doe",
            "date": date(2026,9,18),
            "title": "A Grumpy Cat",
            "excerpt": "The grumpy cat is looking at the camera.",
            "content": """
            Gray cat with a grumpy expression sitting on a wooden surface. 
            
            The cat has a flat face and a frown, giving it a unique and memorable appearance. Its fur is thick and plush, and its eyes are large and round, adding to its grumpy demeanor.
            """
        }
]

def get_date(post):
    return post["date"]

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]  # Get the last 3 posts
    return render(request, "blog/index.html", {"posts": latest_posts})
def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})
def post_detail(request, slug):
    found_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": found_post})