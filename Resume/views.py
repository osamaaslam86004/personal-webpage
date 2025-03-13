import hashlib

from django.shortcuts import render
from django.views.decorators.cache import cache_control


@cache_control(public=True, max_age=604800)  # Cache for 7 days
def custom_get(request):
    """Fastest function-based view for rendering the resume with caching & ETag."""

    response = render(request, "cv.html")  # Directly render template
    response.render()  # Ensure content is fully available before hashing

    # Generate a strong ETag based on content hash
    content_hash = hashlib.md5(response.content).hexdigest()
    response["ETag"] = f'W/"{content_hash}"'

    return response
