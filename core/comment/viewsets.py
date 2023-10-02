from django.http.response import Http404

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.comment.serializers import CommentSerializer
from core.abstract.viewsets import AbstactViewSet

class CommentViewSet(AbstractViewSet):
    http_method_names = ('get', 'post' ,'put' , 'delete')
    permission_classes = (IsAuthenticated)
    serializer_class = CommentSerializer

    