from django.shortcuts import render

def hashtag(request):
    Hashtag.objects.filter(author=request.hastag)


def delete(request):
    note = Note.objects.get(id=request.GET['id'])
    note.delete()

# Create your views here.
