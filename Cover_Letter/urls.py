from django.urls import path
from Cover_Letter.views import RenderCoverLetter


urlpatterns = [
    path(
        "For-Entry-level-Django-Web-Developer/",
        RenderCoverLetter.as_view(),
    ),
]
