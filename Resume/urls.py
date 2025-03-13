from django.urls import path
from django.views.generic import RedirectView

from Resume.views import render_resume

app_name = "Resume"

urlpatterns = [
    path("python-django-web-developer/", render_resume(), name="render-resume"),
    path("", RedirectView.as_view(pattern_name="Resume:render-resume", permanent=True)),
]
