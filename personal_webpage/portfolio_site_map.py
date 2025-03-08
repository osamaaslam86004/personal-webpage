from django.urls import path

from personal_webpage.views import PortfolioSitemap

sitemaps = {
    "portfolio": PortfolioSitemap(),
}
