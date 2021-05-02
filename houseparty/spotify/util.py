from .credentials import REDIRECT_URL,CLIENT_ID,CLIENT_SECRET
from requests import Request,post
from .models import SpotifyToken
from django.utils import timezone
from datetime import timedelta


def get_user_tokens(sessions_id):
    user_tokens = SpotifyToken.objects.filter(user=sessions_id)
    if user_tokens.exists():
        return user_tokens[0]
    else:
        return None

def update_or_create_user_tokens(sessions_id,access_token,token_type,expires_in,refresh_token):
    tokens = get_user_tokens(sessions_id)
    expires_in = timezone.now() + timedelta(seconds=expires_in)

    if tokens:
        tokens.access_token = access_token
        tokens.refresh_token = refresh_token
        tokens.expires_in = expires_in
        tokens.token_type = token_type
        tokens.save(update_field=['access_token','refresh_token','expires_in','token_type'] )
    else:
        tokens = SpotifyToken(user=sessions_id,refresh_token=refresh_token,token_type=token_type,expires_in=expires_in)
        tokens.save()

def is_spotify_authenticated(sessions_id):
    tokens = get_user_tokens(sessions_id)
    if tokens:
        expire = tokens.expires_in
        if expire <= timezone.now():
            refresh_spotify_token(sessions_id)
        return True
    return False

def refresh_spotify_token(sessions_id):
    refresh_token = get_user_tokens(sessions_id)

    response = post("https://accounts.spotify.com/api/token",data={
        'grant_type': 'refresh_token',
        'refresh_token':refresh_token,
        'redirect_uri':REDIRECT_URL,
        'client_id':CLIENT_ID,
        'client_secret':CLIENT_SECRET,
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    refresh_token = response.get('refresh_token')

    update_or_create_user_tokens(sessions_id,access_token,token_type,expires_in,refresh_token)