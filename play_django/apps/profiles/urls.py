from django.conf.urls import url, include
from .views import ProfileRetrieveAPIView 


urlpatterns = [
    url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
]


