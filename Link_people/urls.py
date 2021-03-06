"""Link_people URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import CustomPasswordChangeView

urlpatterns = [
    path('anything-but-admin/', admin.site.urls),

    # User management
    #path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/password/change", CustomPasswordChangeView.as_view(), name="account_password_change"),
    path('accounts/', include('allauth.urls')),

    # Local app
    path('accounts/', include('users.urls')),
    path('', include('pages.urls')),
    path('profile/', include('user_profile.urls')),
    path('jobs/', include('jobs.urls')),
    path('premium/', include('get_premium.urls')),
    path('purchase/', include('orders.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# We only want Debug Toolbar to appear if DEBUG is true so we’ll add logic to display it only in this case
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
