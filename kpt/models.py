from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name=_('Aktywny?'))

    def publish(self):
        self.save()

    def __str__(self):
        return self.title



class Post(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    title = models.CharField(max_length=200)
    text = CKEditor5Field(
        config_name='default',
        verbose_name='Treść artykułu'
    )
    create_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name=_('Aktywny?'))

    def publish(self):
        self.save()

    def __str__(self):
        if self.category:
            return f"{self.title} ({self.category.title})"
        return self.title

