from django.db import models

# Create your models here.


class Factory(models.Model):
    country = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Crosses(models.Model):
    factory = models.ForeignKey(Factory, null=True, blank=True, on_delete=models.CASCADE, related_name="crosses")
    title = models.CharField(null=True, blank=True, max_length=128)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    description = models.TextField(max_length=512)

    def get_factory_name(self):
        return self.factory.name if self.factory else None

    def get_all_review(self):
        return self.reviews.all()

    def __str__(self):
        return str(self.title)


REVIEWS_CHOICES = (
    (1, " * "),
    (2, 2 * " * "),
    (3, 3 * " * "),
    (4, 4 * " * "),
    (5, 5 * " * "),
)


class AnonymousReview(models.Model):
    cross = models.ForeignKey(Crosses, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    rating = models.PositiveIntegerField(null=False, blank=True, choices=REVIEWS_CHOICES)