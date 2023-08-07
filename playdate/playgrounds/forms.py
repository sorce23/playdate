from django import forms
from .models import Playground


class PlaygroundForm(forms.ModelForm):
    class Meta:
        model = Playground
        fields = ["name", "description", "address", "city", "country", "latitude", "longitude", "availability",
                  "price", "website", "rating"]
