from django.conf.urls import url, include
from .views import (
    LoginApiView, RegistrationApiView
)

urlpatterns = [
    #url(r'^users/login/?$', LoginApiView.as_view()),
    url(r'^users/?$', RegistrationApiView.as_view()),
]

