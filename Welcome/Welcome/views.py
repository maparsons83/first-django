from django.shortcuts import render, reverse
from django.contrib.auth.models import User

from Welcome.models import Recipe
from Welcome.models import Author

def homepage(request):
    html = 'homepage.html'

    results = Recipe.objects.all()

    return render(request, html, {'data': results})


def author(request, author_id):
    html = 'author.html'

    author_obj = Author.objects.filter(id=author_id)[0]

    recipes_obj = Recipe.objects.filter(author=author_obj)

    data_obj = {
        'data': {
            'author': author_obj,
            'recipes': recipes_obj
        }
    }
    return render(request, html, data_obj)


def recipes(request, author_id, recipe_name):
    html = 'homepage.html'


    author_obj = Author.objects.all().filter(id=author_id)[0]

    recipes_obj = Recipe.objects.all().filter(author__id=author_obj.id).filter(title=recipe_name)

    data_obj = {
        'data': {
            'author': author_obj,
            'recipes': recipes_obj
        }
    }
    return render(request, html, data_obj)