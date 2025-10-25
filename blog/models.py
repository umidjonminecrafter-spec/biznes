from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("categoriya", kwargs={"slug": self.slug})



class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="news")
    text = models.TextField()
    joylash = models.CharField(

        max_length=255,
        choices=(
            ('car', "Carouselga"),
            ("right", "Right"),
            ("feat", "Featured"),
            ("lat", "Latest"),
            ("tran", "Tranding")
        )
    )
    chop_etish = models.BooleanField(default=True)
    sana = models.DateField()
    img = models.ImageField(upload_to="news/")
    slug = models.SlugField(unique=True, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})



class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.news.title}"










class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Flickr(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='flickr/')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"





class Email(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email
class ViewCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} - {self.news}"
class Meta:
    unique_together = ('user', 'news')

