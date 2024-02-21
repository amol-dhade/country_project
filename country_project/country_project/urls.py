from django.contrib import admin
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from country_app.views import CityViewset, CountryDetailViewset

router = DefaultRouter()
router.register('city', CityViewset, basename='city')
router.register('country', CountryDetailViewset, basename='country')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
