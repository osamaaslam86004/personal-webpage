from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView


class RenderResume(TemplateView):
    template_name = "cv.html"
