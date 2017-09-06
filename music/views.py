from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album} )


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])    
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',{
            'album': album,
            'error_message': "You did not select a valid song"
        }
        )
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album} )


# ***** Not Using a html Template *****
# Note: Not readable code for other programer to use

#def index(request):
#    all_albums = Album.objects.all()
#    html = ''   
 
#    for album in all_albums:
#        url = '/music/' + str(album.id) + '/'
#        html += '<a href="' + url +'">' + album.album_title + '</a><br>'
    
#    return HttpResponse(html)


# ***** Passing a rendered html Template to HttpResponse *****
# Note: It can be shortcutted
# Use: from django.template import loader, from django.http import HttpResponse

#def index(request):
#    all_albums = Album.objects.all()
#    template = loader.get_template('music/index.html')
#    context = {
#        'all_albums': all_albums,
#    }
    
#    return HttpResponse(template.render(context, request))


# ***** Old Detail *****
# def detail(request, album_id):
#    return HttpResponse("<h2>Details for Album ID:" + str(album_id) + "</h2>")


# ***** Using try, except *****
# Use: from django.http import Http404

#def detail(request, album_id):
#    try:
#        album = Album.objects.get(pk=album_id)
#    except Album.DoesNotExist:
#        raise Http404("Album does not exist")
#    return render(request, 'music/detail.html', {'album': album} )
