from django.urls import path
from .views import hello_world_view, get_crosses, retrieve_crosses, sent_anonymous_rating, factory_view

urlpatterns = [
    path("hello/", hello_world_view),
    path("crosses/", get_crosses),
    path("crosses/<int:id>/", retrieve_crosses),
    path("anonymous_rating/", sent_anonymous_rating),
    path("factory/", factory_view)
]