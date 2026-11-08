from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # profile_image = models.FileField(upload_to='profile_images/') # this is for different file types, not just images. If you want to restrict it to images only, you can use ImageField instead of FileField. But for now, we will use FileField to allow any file type.
    profile_image = models.ImageField(upload_to='profile_images/',null=True) # this is for images only. If you want to allow any file type, you can use FileField instead of ImageField. But for now, we will use ImageField to allow only images.