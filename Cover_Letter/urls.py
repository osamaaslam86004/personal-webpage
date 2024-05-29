from django.urls import path
from Cover_Letter.views import RenderCoverLetter


urlpatterns = [
    path(
        "Cover-Letter-for-Entry-level-Django-Web-Developer/",
        RenderCoverLetter.as_view(),
    ),
]
