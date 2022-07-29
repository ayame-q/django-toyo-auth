from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import social_account_added, social_account_updated, social_account_removed
from allauth.socialaccount.models import SocialAccount


@receiver(user_signed_up)
def signed_up(user, **kwargs):
    social_info = SocialAccount.objects.filter(user=user)[0]
    if social_info.provider in ["iniad", "toyo"]:
        user.is_student = social_info.extra_data["is_student"]
        if not user.is_toyo_member:
            user.is_toyo_member = social_info.extra_data["is_toyo_member"]
        if not user.is_iniad_member:
            user.is_iniad_member = social_info.extra_data["is_iniad_member"]
        user.student_id = social_info.extra_data["student_id"]
        user.entry_year = social_info.extra_data["entry_year"]
        user.save()


@receiver(social_account_added)
def account_added(request, sociallogin, **kwargs):
    user = request.user
    social_info = sociallogin.account
    if social_info.provider in ["iniad", "toyo"]:
        user.is_student = social_info.extra_data["is_student"]
        if not user.is_toyo_member:
            user.is_toyo_member = social_info.extra_data["is_toyo_member"]
        if not user.is_iniad_member:
            user.is_iniad_member = social_info.extra_data["is_iniad_member"]
        user.student_id = social_info.extra_data["student_id"]
        user.entry_year = social_info.extra_data["entry_year"]
        user.save()
