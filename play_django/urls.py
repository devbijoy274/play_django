from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('play_django.apps.authentication.urls')),
    url(r'^api/', include('play_django.apps.profiles.urls')),
    url(r'^api/', include('play_django.apps.articles.urls'))
]
