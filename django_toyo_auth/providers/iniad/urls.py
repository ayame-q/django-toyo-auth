from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import INIADProvider


urlpatterns = default_urlpatterns(INIADProvider)
