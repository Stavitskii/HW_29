from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='ads')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Selection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selections')
    name = models.CharField(max_length=100, unique=True)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name

