from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views


schema_view = get_schema_view(
    openapi.Info(
        title="Motion API",
        default_version='v1',
        description="API for Motion Social Platform",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('backend/api/', include('social.urls')),
                  path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
