from django.urls import path, include
from .views import photo_details, photo_edit, photo_delete, photo_add, photo_list

urlpatterns = [
    path("add/<int:pk>", photo_add, name="photo add"),
    path("<int:pk>/", include([
        path("", photo_details, name="photo details"),
        path("edit/", photo_edit, name="photo edit"),
        path("delete/", photo_delete, name="photo delete"),
    ])),
    path("list/", photo_list, name="photo list"),
]
