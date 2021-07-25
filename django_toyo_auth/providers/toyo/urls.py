from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import ToyoProvider


urlpatterns = default_urlpatterns(ToyoProvider)
