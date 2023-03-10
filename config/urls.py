from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="PySoNet API",
        default_version='v1',
        description="Docs",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Pillow (картинки)
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from apps.clients.views import ClientViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('apps.clients.urls')),
    path('shop/', include('apps.shop.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

# router = routers.DefaultRouter()
# router.register(r'api/clients', ClientViewSet)
#
# urlpatterns += router.urls

# Для статики:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

