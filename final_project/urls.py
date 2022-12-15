"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from final_project.category.views import home
from final_project.store.views import product_details

urlpatterns = [
    path('securelogin/', admin.site.urls),
    #    path('', include('final_project.category.urls')),
    path('', home, name='home'),
    path('store/', include('final_project.store.urls'), name='store'),
    path('cart/', include('final_project.carts.urls'), name='cart'),
    path('accounts/', include('final_project.accounts.urls'), name='accounts'),

    # ORDERS
    path('orders/', include('final_project.orders.urls'), name='orders'),

    # Enables browsable API of DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('final_project.store.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
