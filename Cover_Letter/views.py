from django.views.generic import TemplateView


class RenderCoverLetter(TemplateView):
    template_name = "Cover_Letter/cover_letter.html"
