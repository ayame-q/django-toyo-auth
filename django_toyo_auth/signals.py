from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import social_account_added, social_account_updated, social_account_removed
from allauth.socialaccount.models import SocialAccount, SocialToken
import re

@receiver(user_signed_up)
def signed_up(user, **kwargs):
    social_info = SocialAccount.objects.filter(user=user)[0]
    social_token = SocialToken.objects.filter(account=social_info)[0]
    if social_info.provider in ["iniad", "toyo"]:
        user.is_student = social_info.extra_data["is_student"]
        user.student_id = social_info.extra_data["student_id"]
        user.entry_year = social_info.extra_data["entry_year"]
        user.save()

@receiver(social_account_added)
def account_added(request, sociallogin, **kwargs):
    user = request.user
    social_info = sociallogin.account
    social_token = sociallogin.token
    if social_info.provider in ["iniad", "toyo"]:
        user.is_student = social_info.extra_data["is_student"]
        user.student_id = social_info.extra_data["student_id"]
        user.entry_year = social_info.extra_data["entry_year"]
        user.save()
