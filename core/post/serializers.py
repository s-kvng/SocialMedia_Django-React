from rest_framework import serializers 
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.user.serializers import UserSerializer
from core.post.models import Post
from core.user.models import User
 

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset =User.objects.all() , slug_field = 'public_id')
    #allows us to write a custom function that will return a value we want to attribute to this field.
    #these fields are not part of the Post model but are initiated by its methods in the PostSerializer class
    liked = serializers.SerializerMethodField() #get_liked
    likes_count = serializers.SerializerMethodField()
    
    def validate_author(self, value):
        if self.context['request'].user != value:
            raise ValidationError("You can't create a post for another user")
        return value

    #method to get user data ,along with the post data
    def to_representation(self , instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        #It replaces the author field in the representation with the serialized data of the user obtained from UserSerializer.
        rep["author"] = UserSerializer(author).data

        return rep

    #method to update post
    def update(self , instance , validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        
        instance = super().update(instance , validated_data)

        return instance 

    
    def get_liked(self , instance):
        #It first attempts to retrieve the request object from the context 
        request = self.context.get('request' , None)

        if request is None or request.user.is_anonymous:
            return False
        
        return request.user.has_liked(instance)

    
    def get_likes_count(self , instance ):
        return instance.liked_by.count()


    class Meta:
        model = Post
        # List all fields that will be included in a request or a reponse 
        fields = [
            'id' , 'author' , 'body' , 'edited' ,'liked', 'likes_count', 'created_at' , 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'edited']