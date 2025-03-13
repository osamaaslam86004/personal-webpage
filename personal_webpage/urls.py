"""
URL configuration for personal_webpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from personal_webpage.csp_violation_report import csp_violation_report
from personal_webpage.portfolio_site_map import sitemaps
from personal_webpage.views import robots_txt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Resume.urls")),
    path("cover-letter/", include("Cover_Letter.urls")),
    # Content-Security-Policy Violation Reporting
    path("csp-violation-report/", csp_violation_report, name="csp_violation_report"),
    # Robots.txt
    path("robots.txt", robots_txt, name="robots-txt"),
    # SiteMap
    path(
        "python-django-web-developer/sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

# if settings.DEBUG:
#     urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
