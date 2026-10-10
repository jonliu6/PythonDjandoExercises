from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here. The model references should be defined first before the model that references them.
# For example, the Author model should be defined before the Book model since the Book model has a ForeignKey to the Author model.
class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.province} {self.postal_code}"

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True, related_name='books')
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    published_countries = models.ManyToManyField(Country, related_name='books')

    #def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug = slugify(self.title)
    #    super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author} (Rating: {self.rating})"

    def get_absolute_url(self):
        # return reverse('book-detail', args=[str(self.id)])
        return reverse('book-detail', args=[str(self.slug)])