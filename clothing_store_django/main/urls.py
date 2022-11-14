from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:pk>/", views.CatalogDetailView, name="product"),
    path("about", views.about, name="about"),
    path("create", views.create, name="create"),
    path("login", views.login_user, name="login"),
    path("register", views.register_user, name="register"),
    path("logout", views.logout_user, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
