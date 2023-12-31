from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("pages.urls")),
    # path("", include("posts.urls")),
    path("", include("books.urls")),
    path("api/", include("apis.urls")),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("articles/", include("articles.urls")), # new
    path("bankomat/", include("bankomat.urls")),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    