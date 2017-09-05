from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/index.html', {'album': album} )




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


