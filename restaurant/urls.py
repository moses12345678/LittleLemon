from . import views
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('menus', views.MenuViewSet)
router.register('bookings', views.BookingViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/',include(router.urls)),
]