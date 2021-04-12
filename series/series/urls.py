"""series URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from series.views import home, episode_bcs, character, season, season_bb, episode_bb, search_bar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('betterCallSaul/episodes/<int:episode_id>', episode_bcs, name="episode"),
    path('characters/<str:name>', character, name="character"),
    path('betterCallSaul/<int:season>', season, name="season"),
    path('breakingBad/<int:season>', season_bb, name="season_bb"),
    path('breakingBad/episodes/<int:episode_id>', episode_bb, name="episode_bb"),
    path('search', search_bar, name="search"),
]
