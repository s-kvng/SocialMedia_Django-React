from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status

from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.post.serializers import PostSerializer

class PostViewSet(AbstractViewSet):
    http_method_names = ("get","post")
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer


    def get_queryset(self):
        return Post.objects.all()

    def get_object(self):
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request , obj)
        return obj

    def create(self, request , *args , **kwargs ):
        #pass data to the serializer declared in the ViewSet
        serializer = self.get_serializer(data=request.data)

        #validate the data
        serializer.is_valid(raise_exception = True) 

        #create a post object   
        self.perform_create(serializer)
        return Response(serializer.data , status= status.HTTP_201_CREATED)
    
