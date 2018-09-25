"""gbshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from gbshop.views import main
from appAccounts.views import *
from appMain.views import *


router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet)
# router.register(r'categories', ProductCategoriesViewSet)
# router.register(r'lightsources', ProductLightSourcesViewSet)
# router.register(r'manufacturers', ProductManufacturersViewSet)
# router.register(r'resolutions', ProductResolutionsViewSet)
# router.register(r'types', ProductTypesViewSet)
router.register('users', UsersViewSet)

urlpatterns = [
    path('', main),
    path(r'api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
