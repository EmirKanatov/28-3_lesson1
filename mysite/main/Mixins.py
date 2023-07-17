from django.utils.html import format_html


class ImageTagMixin:

    def photo_tag(self, obj):
        if obj.image:
            return format_html(
                '<div style="width: 80px; height: 80px; '
                'border-radius: 50%; overflow: hidden; '
                'margin-right: 10px;">'
                '<img src="{}" style="width: 100%; height: 100%; '
                'object-fit: cover;" />'
                '</div>'.format(obj.image.url)
            )