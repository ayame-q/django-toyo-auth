from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import ToyoProvider


class ToyoOAuth2Adapter(GoogleOAuth2Adapter):
    provider_id = ToyoProvider.id


oauth2_login = OAuth2LoginView.adapter_view(ToyoOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(ToyoOAuth2Adapter)
