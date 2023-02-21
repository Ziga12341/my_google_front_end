from django.shortcuts import render
import markdown2
from .util import list_entries, get_entry, save_entry
from django import forms
from django.http import HttpResponseRedirect


class SearchEntryForm(forms.Form):
    entry = forms.CharField(label="Type entry name you search for:")


def index(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = SearchEntryForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            entry = form.cleaned_data["entry"]

            # return url with entry
            return HttpResponseRedirect(f'/wiki/{entry}')

    return render(request, f"encyclopedia/index.html", {
        "entries": list_entries(),
        "form": SearchEntryForm(),
    })


def show_entry(request, title):
    if title.capitalize() in list_entries() or\
            title.upper() in list_entries() or\
            title.lower() in list_entries():
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(get_entry(title)),
            "page_title": title.capitalize(),
            "form": SearchEntryForm(),
        })

    return render(request, "encyclopedia/entry.html", {
        "entry": f"Error: requested page {title.capitalize()} was not found.\n"
                 f"Use search on left side of the page.",
        "page_title": title.capitalize(),
        "form": SearchEntryForm(),
    })
