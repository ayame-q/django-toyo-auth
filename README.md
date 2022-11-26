# Django Toyo Auth

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
    'django_toyo_auth',
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
```

### urls.py

```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

## Classes

### django_toyo_auth.models.AbstractUser

User class with student_id, entry_year, is_student, is_toyo_member, is_iniad_member

#### Attributes

- student_id
- entry_year
- is_student
- is_toyo_member
- is_iniad_member
- grade

### django_toyo_auth.models.UUIDAbstractUser

Inherits all attributes and methods from [AbstractUser](#django_toyo_authmodelsabstractuser),
but also primary_key is UUID

#### Attributes

- uuid

### django_toyo_auth.admin.ToyoUserAdmin

ModelAdmin class for [AbstractUser](#django_toyo_authmodelsabstractuser).
It offers user-friendly admin pages.

### django_toyo_auth.admin.UUIDToyoUserAdmin

ModelAdmin class for [UUIDAbstractUser](#django_toyo_authmodelsuuidabstractuser).
It offers user-friendly admin pages.

## Details

It offers only providers and custom models for django-allauth.
Please see [django-allauth documents](https://django-allauth.readthedocs.io/en/latest/index.html) for detail

## Requirements

- [Django](https://docs.djangoproject.com/)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)

## License

MIT
