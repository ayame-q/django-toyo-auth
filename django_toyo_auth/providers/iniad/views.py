import requests

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import INIADProvider


class INIADOAuth2Adapter(GoogleOAuth2Adapter):
    provider_id = INIADProvider.id

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(
            self.profile_url,
            params={"access_token": token.token, "alt": "json"},
        )
        resp.raise_for_status()
        extra_data = resp.json()
        login = self.get_provider().sociallogin_from_response(request, extra_data)
        return login


oauth2_login = OAuth2LoginView.adapter_view(INIADOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(INIADOAuth2Adapter)
