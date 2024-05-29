from django.urls import path
from Resume.views import RenderResume
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="render-resume", permanent=True)),
    path("intern-python-web-developer/", RenderResume.as_view(), name="render-resume"),
]
