from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.full_name()
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=100)
    date =models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title