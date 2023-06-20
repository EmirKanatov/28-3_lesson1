from django.db import models

# Create your models here.


class Crosses(models.Model):
    title = models.CharField(null=True, blank=True, max_length=128)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    description = models.TextField(max_length=512)
    rating = models.FloatField(default=5)


    def __str__(self):
        return str(self.title)


class AnonymousReview(models.Model):
    cross = models.ForeignKey(Crosses, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    rating = models.FloatField(default=5)