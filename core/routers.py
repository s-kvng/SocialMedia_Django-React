from rest_framework import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet


"""_summary_
    writing the urls for the endpoints 
"""

router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r"auth/register", RegisterViewSet, basename="auth-register")

router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
]
