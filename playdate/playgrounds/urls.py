from django.urls import path
from .views import playgrounds_list, playground_details, playground_add, playground_edit, playground_delete

urlpatterns = [
    path("", playgrounds_list, name="playgrounds list"),
    path("add/", playground_add, name="playground add"),
    path("<int:pk>/", playground_details, name="playground details"),
    path("<int:pk>/edit/", playground_edit, name="playground edit"),
    path("<int:pk>/delete/", playground_delete, name="playground delete"),
]
