from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    path("", views.google_index, name="google_index"),
    path("image/", views.google_image, name="google_image"),
    path("advanced/", views.google_advanced, name="google_advanced"),
]
