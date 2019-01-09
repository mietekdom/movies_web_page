from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def wszystkie_filmy(request):
    text_views = "to jest tekst z views"
    filmy = ['Terminator', 'Alien', 'Terminator Salvation']
    return render(request, 'lista_filmow.html',
                  {'text': text_views, 'filmy': filmy})

