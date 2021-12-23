from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from apis import views

router = routers.DefaultRouter()
router.register(r'api/logs', views.LogViewSet,basename='log')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
