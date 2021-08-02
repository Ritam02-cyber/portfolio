from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to = 'thumbnail')
    start_date = models.DateField()
    end_date = models.DateField()
    curated_time = models.DateTimeField(auto_now_add=True)
    github_link = models.URLField()
    website_link = models.URLField()
    category = models.ManyToManyField(Category, related_name = 'category')
    def __str__(self):
        return self.name 