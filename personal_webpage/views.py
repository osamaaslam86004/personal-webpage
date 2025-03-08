from django.contrib.sitemaps import Sitemap
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_GET


@require_GET
def robots_txt(request):
    """Generate robots.txt file"""

    content = """
User-agent: *
Disallow: /admin/
Disallow: /csp-violation-report/
Disallow: /cover-letter/
Disallow: /static/Resume/images/favicon-16x16.png

User-agent: GPTBot
Disallow: /

Sitemap: https://personalwebpage.pythonanywhere.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")


class PortfolioSitemap(Sitemap):
    """Generate Sitemap for website"""

    priority = 0.8  # Higher priority for main pages
    changefreq = "weekly"  # Frequency of updates

    def items(self):
        return ["Resume:render-resume"]  # Name of the URL pattern in urls.py

    def location(self, item):
        return reverse(item)
