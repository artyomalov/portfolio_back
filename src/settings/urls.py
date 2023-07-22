from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('projects.urls')),
    path('api/v1/', include('services.urls')
         )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
