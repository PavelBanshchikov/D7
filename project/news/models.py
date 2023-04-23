from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Author (models.Model):
    rating = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class Category (models.Model):
    type_of_news = models.CharField(max_length = 255, unique = True)
    subscribers = models.ManyToManyField(User, related_name='categories')

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    time_in = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    header = models.CharField(max_length = 255)
    text_post = models.TextField()
    rating_post = models.IntegerField(default = 0)
    NEWS = 'NW'
    ARTICAL = 'AR'
    CATEGORY_CHOICES = ((NEWS, "Новость"), (ARTICAL, 'Статья'))
    category_type = models.CharField(max_length = 2, choices = CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.header}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[0:100] + '...'

class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text_comment = models.TextField()
    time_in = models.DateTimeField(auto_now_add = True)
    rating_comment = models.IntegerField(default = 0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )