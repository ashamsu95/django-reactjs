from django.urls import path
from .views import AuthURl,spotify_callback,Is_Authenticated

urlpatterns = [
    path('get-auth-url',AuthURl.as_view()),
    path('redirect',spotify_callback),
    path('is-authenticated',Is_Authenticated.as_view()),
]