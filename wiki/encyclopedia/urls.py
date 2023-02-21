from django.urls import path

from .views import show_entry, index

app_name = "wiki"
urlpatterns = [
    path("", index, name="index"),
    path("<str:title>", show_entry, name="entries"),
]
