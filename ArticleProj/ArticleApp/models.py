from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateTimeField('publication date')
    category = models.CharField(max_length=200)
    hero_image_name = models.CharField(max_length=200)
    optional_image_name = models.CharField(max_length=200)
    body_text = models.TextField()

