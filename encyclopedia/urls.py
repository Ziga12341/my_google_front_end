from django.urls import path

from encyclopedia.views import entries, index

urlpatterns = [
    path("", index, name="index"),
    path("<str:title>", entries, name="entries"),
]
