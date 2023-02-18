from django.shortcuts import render
import markdown2
from encyclopedia.util import list_entries, get_entry, save_entry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries()
    })


def entries(request, title):
    if title.capitalize() in list_entries() or\
            title.upper() in list_entries() or\
            title.lower() in list_entries():
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(get_entry(title)),
            "page_title": title.capitalize(),
        })
    return render(request, "encyclopedia/error_page.html", {
        "error": f'Error: requested page "{title.capitalize()}" was not found',
    })