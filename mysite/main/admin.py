from django.contrib import admin
from .models import Crosses, AnonymousReview, Factory
# Register your models here.


@admin.register(Crosses)
class CoursesAdmin(admin.ModelAdmin):
    fields = ['title', "id", 'description', 'factory', 'price']


@admin.register(AnonymousReview)
class AnonymousReviewAdmin(admin.ModelAdmin):
    fields = ['title', "id", 'description', 'cross', 'rating']


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    fields = ["country", "name", "description"]