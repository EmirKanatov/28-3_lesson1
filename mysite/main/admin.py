from django.contrib import admin

from .Mixins import ImageTagMixin
from .models import Crosses, AnonymousReview, Factory
# Register your models here.


@admin.register(Crosses)
class CoursesAdmin(admin.ModelAdmin, ImageTagMixin):
    list_display = ['title', 'photo_tag']
    fields = ['title', 'description', 'photo_tag', 'image', 'factory', 'price']
    readonly_fields = ['photo_tag']


@admin.register(AnonymousReview)
class AnonymousReviewAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'cross', 'rating']


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    fields = ["country", "name", "description"]