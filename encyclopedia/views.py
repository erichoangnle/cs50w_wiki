from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import choice
import markdown2

from . import util


def index(request):
    """
    Render main app template with a list of all articles in database.
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request):
    """
    Search database for query string. If article title match query string,
    redirect user to coresponding article page. Else, redirect user to Search
    Result page where all articles with query string as sub-string will be listed.
    """
    if request.method == 'POST':
        if util.get_entry(request.POST['q']):
            entry = request.POST['q']
            return HttpResponseRedirect(f"/wiki/{entry}")
        else:
            entries = util.list_entries()
            search_result = []
            for entry in entries:
                if request.POST['q'].lower() in entry.lower():
                    search_result.append(entry)
            return render(request, "encyclopedia/search.html", {
                "results": search_result
            })

def new_page(request):
    """
    If request method is GET, render a page where user can enter information
    for a new article. If request methos is POST, first check if article title
    provided by user match any artical in database. If matched, redirect user to
    an Error Page, saying article already exist. Else, write user input to database
    as MARKDOWN file, and then redirect user to newly create article page.
    """
    if request.method == 'POST':
        title = request.POST['title']
        entries = util.list_entries()
        for entry in entries:
            if title.lower() == entry.lower():
                return render(request, 'encyclopedia/entry.html', {
                    'entry': "Entry already exist."
                })
        with open(f"entries/{title}.md", mode='w', newline='') as file:
            file.write(request.POST['entry'])
        return HttpResponseRedirect(f"/wiki/{title}")
    else:
        return render(request, "encyclopedia/new_page.html")

def edit_page(request, title):
    """
    If request method is GET, redirect user to a page with textarea already
    populated with article's entry where user can edit article. If request
    methos is POST, write new editted entry to database and redirect user
    to coresponding article page.
    """
    if request.method == 'POST':
        with open(f"entries/{title}.md", mode='w', newline='') as file:
            file.write(request.POST['entry'])
        return HttpResponseRedirect(f"/wiki/{title}")
    else:
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            'title': title,
            'entry': entry
        })

def entry(request, title):
    """
    Render article page using title. If article does not already exist in database,
    show an error message.
    """
    if util.get_entry(title):
        entry = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": "Entry does not exist"
        })

def random(request):
    """
    Redirect user to a random article page in database.
    """
    title = choice(util.list_entries())
    return HttpResponseRedirect(f"/wiki/{title}")