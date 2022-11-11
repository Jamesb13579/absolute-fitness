from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    membership = models.ForeignKey('Memberships', null=True, blank=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Memberships(models.Model):

    class Meta:
        verbose_name_plural = 'Memberships'

    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name

