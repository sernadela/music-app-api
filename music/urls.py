"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from musicapp import views

router = routers.DefaultRouter()

router.register(r'api/v1/users', views.UserViewSet)  # CRUD actions for users
router.register(r'api/v1/songs', views.SongViewSet)  # CRUD actions for songs


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api/v1/fav/user/(?P<user>[0-9]+)/song/(?P<song>[0-9]+)', views.FavSongView.as_view()),  # ADD Song to User
    url(r'api/v1/fav/user/(?P<user>[0-9]+)/song', views.FavSongView.as_view()),  # RM Song from User
    url(r'api/v1/fav/user/(?P<user>[0-9]+)', views.FavSongView.as_view()),  # Get User Fav Songs
]
