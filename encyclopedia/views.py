from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entries(request, title):
    if title.capitalize() or title.uppercase() or title.lowercase in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(util.get_entry(title)),
            "page_title": title.capitalize(),
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": f"Error: requested page {title.capitalize()} was not found",
            "page_title": title.capitalize(),
        })