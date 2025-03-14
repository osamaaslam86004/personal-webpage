import hashlib
import os
from datetime import datetime, timezone

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.http import condition

# Path to the template file
TEMPLATE_PATH = os.path.join(settings.BASE_DIR, "templates", "cv.html")
print(TEMPLATE_PATH, settings.BASE_DIR)


def etag_func(request, *args, **kwargs):
    """Generate an ETag based on the rendered template content hash."""
    try:
        with open(TEMPLATE_PATH, "rb") as f:
            content = f.read()
        return hashlib.md5(content).hexdigest()
    except FileNotFoundError:
        return None  # If template file doesn't exist, no ETag


def last_modified_func(request, *args, **kwargs):
    """Return the last modified timestamp of the template file."""
    try:
        modified_time = os.path.getmtime(TEMPLATE_PATH)
        return datetime.fromtimestamp(
            modified_time, timezone.utc
        )  # Convert to UTC datetime
    except FileNotFoundError:
        return None



@cache_control(public=True, max_age=604800)  # Cache for 7 days)
@condition(etag_func=etag_func, last_modified_func=last_modified_func)
def render_resume(request):
    """Render the resume page, detecting template changes."""
    return render(request, "Resume/cv.html")
  
