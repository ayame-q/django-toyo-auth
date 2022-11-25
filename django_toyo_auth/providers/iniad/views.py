from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import INIADProvider


class INIADOAuth2Adapter(GoogleOAuth2Adapter):
    provider_id = INIADProvider.id


oauth2_login = OAuth2LoginView.adapter_view(INIADOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(INIADOAuth2Adapter)
