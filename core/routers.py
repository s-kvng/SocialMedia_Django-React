from rest_framework_nested import routers

from core.user.viewsets import UserViewSet
from core.post.viewsets import PostViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.comment.viewset import CommentViewSet


"""_summary_
    writing the urls for the endpoints 
"""

router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")


# ##################################################################### #
# ###################       POST       ###################### #
# ###########
router.register(r"post", PostViewSet , basename="post")

posts_router = routers.NestedSimpleRouter(router , r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet , basename="post-comment")


router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
    *posts_router.urls,
]
