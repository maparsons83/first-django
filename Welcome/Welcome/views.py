from django.shortcuts import render, reverse
from django.contrib.auth.models import User

from Welcome.models import Recipe
from Welcome.models import Author

def homepage(request):
    html = 'homepage.html'

    results = Recipe.objects.all()

    return render(request, html, {'data': results})