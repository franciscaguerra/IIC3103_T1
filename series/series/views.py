from django.http import HttpResponse
from django.template import Template, Context
import requests
from django.shortcuts import render


def home(request):
    episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul").json()
    episodes_bb = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad").json()
    temporadas = []
    temporadas_bb = []
    for episode in episodes:
        temporadas.append(episode["season"])
    seasons = list( dict.fromkeys(temporadas))
    for e in episodes_bb:
        temporadas_bb.append(e["season"])
    seasons_bb = list( dict.fromkeys(temporadas_bb))
    return render(request, 'home.html', {'seasons': seasons, 'seasons_bb': seasons_bb})


def season(request, season):
    episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul").json()
    season = str(season)
    return render(request, 'season.html', {'episodes': episodes, 'season': season})

def season_bb(request, season):
    episodes = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad").json()
    season = str(season)
    return render(request, 'season.html', {'episodes': episodes, 'season': season})

def episode_bcs(request, episode_id):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/%s' % episode_id
    episode = requests.get(url).json()[0]
    return render (request, 'episode_bcs.html', {"episode": episode})

def episode_bb(request, episode_id):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/%s' % episode_id
    episode = requests.get(url).json()[0]
    return render (request, 'episode_bb.html', {"episode": episode})

def character(request, name):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=%s' % name
    character = requests.get(url).json()[0]
    url_quote = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=%s' % name
    quotes = requests.get(url_quote).json()
    if len(quotes) == 0:
        quotes = 0
    if len(character["appearance"]) == 0:
        character["appearance"] = -1
    if len(character["better_call_saul_appearance"]) == 0:
        character["better_call_saul_appearance"] = -1
    return render (request, 'character.html', {'character': character, 'quotes': quotes})


def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=%s' % searched

    result = requests.get(url).json()
    return render(request, 'search_bar.html', {'result': result})