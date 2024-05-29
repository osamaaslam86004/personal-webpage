from django.views.generic import TemplateView


class RenderCoverLetter(TemplateView):
    template_name = "cover_letter.html"
