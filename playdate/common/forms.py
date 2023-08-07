from django import forms
from .models import Comment
from ..playgrounds.models import Country


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_text",)
        widgets = {
            "comment_text": forms.Textarea(
                attrs={
                    "placeholder": "Add comment...",
                })
        }


class SearchForm(forms.Form):
    country_choices = Country.choices()
    country = forms.ChoiceField(choices=country_choices)
