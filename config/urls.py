from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



schema_view = get_schema_view(
   openapi.Info(
      title="Saidoff Group",
      default_version='v1',
      description="Saidoff Group offical website",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #appss
   path('admin/', admin.site.urls),
   path('service/',include('service_app.urls')),
   path('',include('main_app.urls')),
   path('i18n/', include('django.conf.urls.i18n')),
 
]

urlpatterns += i18n_patterns(
    path('set_language/', include('django.conf.urls.i18n')),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

