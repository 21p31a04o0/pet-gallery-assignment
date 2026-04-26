from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet, random_dog, breed_dog

router = DefaultRouter()
router.register('favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dogs/random/', random_dog),
    path('dogs/<str:breed>/', breed_dog),
]