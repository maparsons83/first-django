from django.shortcuts import render, reverse
from django.contrib.auth.models import User

from Welcome.models import Recipe
from Welcome.models import Author
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

def login_view(request):
    html = 'login.html'

    form = Login_Form(None or request.POST)

    if form.is_valid():
        next = request.POST.get('next')
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect(reverse('homepage'))
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/')

    return render(request, html, {'form':form})

def logout_view(request):
    html = 'logout.html'
    logout(request)

    return render(request, html)