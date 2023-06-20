from django.contrib import admin
from .models import Crosses, AnonymousReview
# Register your models here.


@admin.register(Crosses)
class CoursesAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'rating']


@admin.register(AnonymousReview)
class AnonymousReviewAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'cross', 'rating']