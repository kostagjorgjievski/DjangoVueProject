
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
fom django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vi/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
] + static(settigns.MEDIA_URL, document_root=settigns.MEDIA_ROOT)


