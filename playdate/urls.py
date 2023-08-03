from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("playdate.common.urls")),
    path("accounts/", include("playdate.accounts.urls")),
    path("playgrounds/", include("playdate.playgrounds.urls")),
    path("photos/", include("playdate.photos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
