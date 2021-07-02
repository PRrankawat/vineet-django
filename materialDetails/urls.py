from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'materialDetails', MaterialDetailsAPIViewSet)
urlpatterns = router.urls