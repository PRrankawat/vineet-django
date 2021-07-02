from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'siteDetails', SiteDetailsAPIViewSet)
urlpatterns = router.urls