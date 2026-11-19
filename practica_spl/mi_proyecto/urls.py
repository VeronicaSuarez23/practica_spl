from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html')),
]

if settings.ENABLE_REPORTS:
    urlpatterns += [path('reportes/', include('reportes.urls'))]
if settings.ENABLE_NOTIFICATIONS:
    urlpatterns += [path('notificaciones/', include('notificaciones.urls'))]