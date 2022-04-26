from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MainApp import settings
#Подключаем юрл адрес, который ведет к юрл адресам в папке blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)