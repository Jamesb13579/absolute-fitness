from django.db import models

DAY  = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
    )

class trainers(models.Model):
    name = models.CharField(max_length=254)
    about = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class classes(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    time = models.TimeField()
    day_of_week = models.IntegerField(choices=DAY, default=0)
    trainers = models.ForeignKey(trainers, null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class gym(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



