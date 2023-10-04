from django.http.response import Http404

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import raise_exception
from rest_framework import status

from core.comment.serializers import CommentSerializer
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment

class CommentViewSet(AbstractViewSet):
    http_method_names = ('get', 'post' ,'put' , 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        #check if the user is a superuser
        if self.request.user.is_superuser:
            return Comment.objects.all()

        #retrieve the public_id of the post from the url/ kwargs(dictionary containing additional data)
        post_pk = self.kwargs['post_pk']
        if post_pk is None:
            return Http404
        queryset = Comment.objects.filter(post__public_id=post_pk)

        return queryset
    
    def get_object(self):
        comment = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,comment)
        return comment

    def create(self, request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data , status=status.HTTP_201_CREATED)
    