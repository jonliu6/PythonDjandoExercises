from django import forms

class ProfileForm(forms.Form):
    # profileImg = forms.FileField() # used for FileField, which is used for uploading files. If you want to restrict it to images only, you can use ImageField instead of FileField. But for now, we will use FileField to allow any file type.
    profileImg = forms.ImageField() # used for ImageField, which is used for uploading images. If you want to allow any file type, you can use FileField instead of ImageField. But for now, we will use ImageField to allow only images.