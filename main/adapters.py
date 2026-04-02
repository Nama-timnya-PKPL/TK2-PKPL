import uuid
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.core.exceptions import ImmediateHttpResponse
from allauth.account.models import EmailAddress
from django.shortcuts import redirect
from django.contrib.auth import login

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        if request.user.is_authenticated:
            return

        email = sociallogin.user.email
        if not email:
            return

        try:
            existing = EmailAddress.objects.get(email=email)
            sociallogin.connect(request, existing.user)
            login(request, existing.user, backend='django.contrib.auth.backends.ModelBackend')
            raise ImmediateHttpResponse(redirect('/'))
        except EmailAddress.DoesNotExist:
            pass

    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        if not user.username:
            base = (user.email or '').split('@')[0]
            user.username = f"{base}_{uuid.uuid4().hex[:6]}"
        return super().save_user(request, sociallogin, form)