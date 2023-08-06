from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from playdate.photos.models import Photo
from .models import Like, Comment
from .forms import CommentForm, SearchForm
from ..accounts.models import PlaydateUser


def index(request):
    photos = Photo.objects.all()
    users = PlaydateUser.objects.all()

    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data["search_text"]
        photos = photos.filter(playground_name__name__icontains=search_text)

    if request.user.is_authenticated:

        for photo in photos:
            photo.liked_by_user = photo.like_set \
                .filter(user=request.user) \
                .exists()

    context = {
        "users": users,
        "all_photos": photos,
        "comment_form": CommentForm(),
        "search_form": search_form,
    }

    return render(request, "base/index.html", context=context)


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

    # http://127.0.0.1:8000/
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
            print("form is valid")

            new_comment_instance = form.save(commit=False)
            new_comment_instance.to_photo = photo
            new_comment_instance.user = request.user
            new_comment_instance.save()

        return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")
