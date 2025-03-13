import hashlib

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView


@method_decorator(cache_control(public=True, max_age=604800), name="dispatch")
class RenderResume(TemplateView):
    template_name = "cv.html"

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        content_hash = hashlib.md5(response.content).hexdigest()  # Fast and reliable
        response["ETag"] = f'W/"{content_hash}"'  # Weak ETag
        return response
