from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True),
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.author}'


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='comments')
    comment_owner = models.CharField(max_length=100)
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name='comments')
    comment = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f'self.rating - {self.comment_owner} - {self.comment}'
