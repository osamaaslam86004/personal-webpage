from django.shortcuts import render
from django.views.generic import TemplateView


class RenderResume(TemplateView):
    template_name = "cv.html"
