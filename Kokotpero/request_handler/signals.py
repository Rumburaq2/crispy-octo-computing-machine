from allauth.socialaccount.signals import pre_social_login
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from django.core.exceptions import PermissionDenied

@receiver(pre_social_login)
def restrict_by_email_domain(sender, request, sociallogin, **kwargs):
    email_domain = 'gyarab.cz'
    email = sociallogin.account.extra_data.get('email', '')

    if not email.endswith('@' + 'student.gyarab.cz'):
        # If the email does not end with '@gyarab.cz', deny access
        raise PermissionDenied('Access denied. Only @gyarab.cz emails are allowed.')

    # If user is on path overview: Zavolej check_superuser

'''def check_superuser(sender, request, sociallogin, kwargs):
    print("check_superuser")
    # If user is on path overview:
     #check is user = superuser
      #if no: raise PermissionDenied('Access denied. Only @gyarab.cz emails are allowed.')'''