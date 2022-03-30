from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

apipatterns = [
    path('', include('users.urls')),
    path('', include('recipes.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apipatterns)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATICFILES_DIRS
    )
