from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Playground
from .forms import PlaygroundForm
from playdate.photos.models import Photo


def playgrounds_list(request):
    playgrounds = Playground.objects.all().order_by("country", "city")
    context = {"playgrounds": playgrounds}
    return render(request, "playgrounds/playgrounds-list.html", context)


def playground_details(request, pk):
    playground = get_object_or_404(Playground, pk=pk)
    photos = Photo.objects.filter(playground=playground)

    context = {
        "playground": playground,
        "photos": photos,
        "user": request.user,
    }
    return render(request, "playgrounds/playground-details.html", context)


@login_required
def playground_add(request):
    if request.method == "POST":
        form = PlaygroundForm(request.POST)
        if form.is_valid():
            playground = form.save(commit=False)
            playground.owner = request.user
            playground.save()
            return redirect("playground details", pk=playground.pk)
    else:
        form = PlaygroundForm()
    context = {"form": form}
    return render(request, "playgrounds/playground-add.html", context)


@login_required
def playground_edit(request, pk):
    playground = get_object_or_404(Playground, pk=pk)
    if request.method == "POST":
        form = PlaygroundForm(request.POST, instance=playground)
        if form.is_valid():
            form.save()
            return redirect("playground details", pk=playground.pk)
    else:
        form = PlaygroundForm(instance=playground)
    context = {
        "form": form,
        "playground": playground,
    }
    return render(request, "playgrounds/playground-edit.html", context)


@login_required
def playground_delete(request, pk):
    playground = get_object_or_404(Playground, pk=pk)
    if request.method == "POST":
        playground.delete()
        return redirect("playgrounds list")
    context = {"playground": playground}
    return render(request, "playgrounds/playground-delete.html", context)
