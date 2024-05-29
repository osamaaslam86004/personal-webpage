from django.urls import path
from Resume.views import RenderResume


urlpatterns = [
    path("intern-python-web-developer/", RenderResume.as_view(), name="render-resume"),
]
