from rest_framework import serializers 
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.user.serializers import UserSerializer
from core.post.models import Post
from core.user.models import User
 

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset =User.objects.all() , slug_field = 'public_id')

    def validate_author(self, value):
        if self.context['request'].user != value:
            raise ValidationError("You can't create a post for another user")
        return value

    def to_representation(self , instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data

        return rep

    class Meta:
        model = Post
        # List all fields that will be included in a request or a reponse 
        fields = [
            'id' , 'author' , 'body' , 'edited' , 'created_at' , 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']