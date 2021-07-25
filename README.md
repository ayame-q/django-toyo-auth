"Django Toyo Auth" offers providers of Toyo University Accounts(@toyo.jp) and INIAD Accounts(@iniad.org) for [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)


## Installation
### Install Package
```bash
pip install django-toyo-auth
```

### settings.py
```python
INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_toyo_auth', # Offers Custom UserModel
    'django_toyo_auth.providers.iniad', # INIAD Account
    'django_toyo_auth.providers.toyo', # Toyo Account
    ...
]

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'iniad': { # for INIAD Account
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
    'toyo': { # for Toyo Account
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
}

AUTH_USER_MODEL = 'django_toyo_auth.User' # Use custom user model with student id (Optional)
```

### urls.py
```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

## Details
It offers only providers and custom models for django-allauth.
Please see [django-allauth documents](https://django-allauth.readthedocs.io/en/latest/index.html) for detail

## Requirements
* [Django](https://docs.djangoproject.com/)
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)

## Licenses
MIT