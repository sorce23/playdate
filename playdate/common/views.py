from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from playdate.photos.models import Photo
from .models import Like, Comment
from .forms import CommentForm, SearchForm
from ..accounts.models import PlaydateUser
from ..playgrounds.models import Playground


def index(request):
    form = SearchForm()
    users = PlaydateUser.objects.all()

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data["country"]
            playgrounds = Playground.objects.filter(country=country).order_by("city")
        else:
            playgrounds = Playground.objects.all()
    else:
        country = request.GET.get("country")
        if country:
            playgrounds = Playground.objects.filter(country=country).order_by("city")
        else:
            playgrounds = Playground.objects.all()

    context = {
        "playgrounds": playgrounds,
        "form": form,
        "comment_form": CommentForm(),
        "users": users,
    }

    return render(request, "base/index.html", context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    kwargs = {
        "to_photo": photo,
        "user": request.user
    }

    like_object = Like.objects \
        .filter(**kwargs) \
        .first()

    if like_object:
        like_object.delete()
    else:
        new_like_object = Like(**kwargs)
        new_like_object.save()

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")


@login_required
def share_functionality(request, photo_id):

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")


@login_required
def comment_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment_instance = form.save(commit=False)
            new_comment_instance.to_photo = photo
            new_comment_instance.user = request.user
            new_comment_instance.save()

        return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")
