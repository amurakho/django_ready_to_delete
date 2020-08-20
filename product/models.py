from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.fields import AutoSlugField
import os


from product.utils import unique_slug_generator, get_product_image_dir_path


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title', slugify_function=unique_slug_generator)
    code = models.IntegerField(unique=True)
    date_added = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # mean_rating = models.IntegerField(null=True, blank=True, default=0)
    #
    # def some(self):
    #     revs = self.set_review.all()
    #     ratings = [int(rating) for rating in revs.ratings]
    #     return sum(ratings)/len(ratings)

    def __str__(self):
        return f'{self.title}_{self.code}'


class Review(models.Model):
    RANK_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.CharField(choices=RANK_CHOICE, max_length=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='rew_images', null=True, blank=True)


class ProductImage(models.Model):
    image = models.ImageField(upload_to=get_product_image_dir_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)