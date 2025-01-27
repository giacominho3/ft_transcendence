"""
URL configuration for django_progect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView # new
from frontend.views import index # new

# from django_prometheus import exports # new For prometheus to delete

urlpatterns = [
    path("", include("frontend.urls")),
    path('admin/', admin.site.urls),
    # path("chat/", include("chat.urls")), # new
    path('friend/', include('friends.urls')), #new
    path("pong/", include("pong.urls")), # new
    path("accounts/", include("accounts.urls")), # new
    path("accounts/", include("django.contrib.auth.urls")), # new
    # path('metrics', exports.ExportToDjangoView, name='prometheus-django-metrics'), # For prometheus to delete
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', include("frontend.urls"), name='index')]