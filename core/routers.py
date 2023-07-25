from rest_framework import routers

from core.user.viewsets import UserViewSet

"""_summary_
    writing the urls for the endpoints 
"""

router = routers.SimpleRouter()
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
]
