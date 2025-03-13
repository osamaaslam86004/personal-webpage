from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView


@method_decorator(cache_control(public=True, max_age=604800), name="dispatch")
class RenderResume(TemplateView):
    template_name = "cv.html"
