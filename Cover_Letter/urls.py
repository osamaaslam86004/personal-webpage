from django.urls import path
from Cover_Letter.views import RenderCoverLetter
from django.views.generic import RedirectView

urlpatterns = [
    path(
        "For-Entry-level-Django-Web-Developer/",
        RenderCoverLetter.as_view(),
        name="Entry-level-Django-Web-Developer",
    ),
    path(
        "",
        RedirectView.as_view(
            pattern_name="Entry-level-Django-Web-Developer", permanent=True
        ),
    ),
]
