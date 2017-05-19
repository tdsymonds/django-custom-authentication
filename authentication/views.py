# -*- coding: utf-8 -*- 
from django.conf import settings
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, 
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'authentication/pages/_login.html'


class CustomLogoutView(LogoutView):
    next_page = 'authentication:login'


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'authentication/emails/password_reset_email.html'
    extra_email_context = {'site_url': settings.SITE_URL }
    html_email_template_name = 'authentication/emails/password_reset_email_html.html'
    success_url = reverse_lazy('authentication:password_reset_done')
    template_name = 'authentication/pages/_password_reset.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('authentication:password_reset_complete')
    template_name = 'authentication/pages/_password_reset_confirm.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/pages/_password_reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'authentication/pages/_password_reset_complete.html'
