from django.conf import settings
from django.urls import path
from appgallery import views
from django.conf.urls.static import static
# from appgallery.views import gallery

urlpatterns = [
    path('', views.gallery),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)