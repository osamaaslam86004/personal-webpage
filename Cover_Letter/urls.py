from django.urls import path
from django.views.generic import RedirectView

from Cover_Letter.views import RenderCoverLetter

app_name = "Cover_Letter"
urlpatterns = [
    path(
        "cover-letter-for-python-django-web-developer/",
        RenderCoverLetter.as_view(),
        name="python-django-web-developer-cover-letter",
    ),
    path(
        "",
        RedirectView.as_view(
            pattern_name="Cover_Letter:python-django-web-developer-cover-letter",
            permanent=True,
        ),
    ),
]
