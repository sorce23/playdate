from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from playdate.common.forms import CommentForm
from .forms import PhotoAddForm, PhotoEditForm
from .models import Photo
from ..playgrounds.models import Playground

UserModel = get_user_model()


@login_required
def photo_list(request):
    user = request.user
    photos = Photo.objects.filter(user=user)

    context = {"photos": photos}

    return render(request, "photos/photo_list.html", context)


@login_required
def photo_add(request, pk):
    playground = Playground.objects.get(pk=pk)
    form = PhotoAddForm()

    if request.method == "POST":
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.playground = playground
            photo.save()
        return redirect("playground details", pk=pk)
    else:
        form = PhotoAddForm(initial={"playground": playground})

    context = {
        "form": form,
        "playground": playground,
    }

    return render(request, "photos/photo-add.html", context)


@login_required
def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        "user": request.user,
        "photo": photo,
        "likes": photo.like_set.count(),
        "comments": photo.comment_set.all(),
        "comment_form": comment_form,
    }

    return render(
        request,
        "photos/photo-details.html",
        context=context
    )


@login_required
def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(instance=photo)

    if request.method == "POST":
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("photo details", pk=pk)

    context = {
        "photo": photo,
        "form": form,
    }

    return render(request, "photos/photo-edit.html", context)


@login_required
def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)

    if request.method == "POST":
        photo.delete()
        return redirect("index")

    context = {"photo": photo}
    return render(request, "photos/photo-delete.html", context)
