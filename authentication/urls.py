# -*- coding: utf-8 -*- 
from django.conf.urls import url

from .views import (CustomLoginView, CustomLogoutView, CustomPasswordResetView, 
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomPasswordResetDoneView)


urlpatterns = [    
    url(r'^login/$', CustomLoginView.as_view(), name='login'),
    url(r'^logout/$', CustomLogoutView.as_view(), name='logout'),
    url(r'^password/reset/$', CustomPasswordResetView.as_view(), name='password_reset'),
    url(r'^password/reset/done/$', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password/reset/complete/$', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
