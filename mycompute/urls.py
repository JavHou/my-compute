"""mycompute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from compute import views
urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('computev1/',views.computev1),
    path('compute-ajax/',views.compute_ajax),
    path('result/',views.result),
    path('compute-history/',views.compute_history),
    path('result-history/', views.result_history),
    path('login/',views.login),
    # path('favicon.ico/', RedirectView.as_view(url=r'static/favicon.ico')),
]
