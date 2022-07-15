from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class Foods(models.Model):
    photo = models.ImageField(upload_to='image/', blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('foods_detail', args=[str(self.id)])

    class Meta:
        ordering = ('name',)
        index_together = (('id',),)


