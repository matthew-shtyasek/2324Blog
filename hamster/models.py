from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=115, validators=[MinLengthValidator(12)], verbose_name='Название')
    text = models.TextField(null=False, blank=False, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    change_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    categories = models.ManyToManyField('Category', related_name='posts')
    likes = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=46, validators=[MinLengthValidator(3)], verbose_name='Название')

    def __str__(self):
        return self.name