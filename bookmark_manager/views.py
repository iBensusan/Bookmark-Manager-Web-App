from django.shortcuts import render, redirect
from bookmarks.models import Bookmark

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        new_bookmark = Bookmark(title=title, url=url)
        new_bookmark.save()
        return redirect('bookmark_list')

    return render(request, 'bookmarks/bookmark_list.html', {'bookmarks': bookmarks})

def delete_bookmark(request, id):
    bookmark = Bookmark.objects.get(id=id)
    bookmark.delete()
    return redirect('bookmark_list')
