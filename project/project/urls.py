from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    # Делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py)
    # подключались к главному приложению с префиксом products/.
    path('products/', include('simpleapp.urls')),
    #урл для приложений для аунтификации
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    # Подключение allauth
    path('accounts/', include('allauth.urls')),
]
