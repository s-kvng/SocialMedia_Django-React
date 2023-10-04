from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from core.abstract.serializers import AbstractSerializer
from core.user.serializers import UserSerializer
from core.comment.models import Comment
from core.user.models import User
from core.post.models import Post


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="public_id")
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field="public_id")


    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError('You cant create a comment for another user')
        return value

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return  value


    '''return user object along with the comment object'''
    def to_representation(self , instance):
        #get the default object of the comment
        rep = super().to_representation(instance)
        #retrieve the author object of the comment 
        author = User.objects.get_object_by_public_id(rep["author"])
        #add the user object as a value of the author key
        rep["author"] = UserSerializer(author).data

        return rep

    '''Update comment'''
    def update(self , instance , validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance
    
    class Meta:
        model = Comment
        ''' list all fields to be included in the request and response '''
        fields = [
            'id', 'post' , 'author' , 'body' , 'edited' , 'created_at' , 'updated_at'
        ]
        read_only_fields =['edited ']