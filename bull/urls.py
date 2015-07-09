"""bull URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r-'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from bull import api_urls
from bull.views import Home
from members import urls as member_urls
from booking import urls as booking_urls

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_urls, namespace='api')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include(member_urls, namespace='members')),
    url(r'^ovingsspeil/', include(booking_urls, namespace='booking')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
