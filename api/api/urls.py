from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/', index, name='index'),
    path('auth/', include('authapp.urls')),
    path('', include('chat.urls')),
    path('email/', include('emailapi.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
