from django.urls import path, include
from .views import SignUpView
from django.views.generic.base import TemplateView

urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]