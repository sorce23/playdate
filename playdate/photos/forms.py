from django import forms
from .models import Photo

labels = {
    "playground_image": "Photo file",
    "description": "Description",
    "location": "Location",
    "playground_name": "Playground",
}


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["playground_image", "description", "location", "playground_name"]
        labels = labels


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["description", "location", "playground_name"]
        exclude = ["playground_image"]
        labels = labels
