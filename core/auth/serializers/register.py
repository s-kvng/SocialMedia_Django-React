from rest_framework import serializers

from core.user.serializers import UserSerializer
from core.user.models import User


class RegisterSerializer(UserSerializer):
    """_summary_

    Args:
        UserSerializer (_type_): Registration serializer for requests and user creation
    """

    # Required password to have max value of 128 & not less than 8 characters,
    # should not be able to be read
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = User
        # list all fields that can be included in a request or a response
        fields = [
            "id",
            "bio",
            "avatar",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
        ]

    def create(self, validated_data):
        # use the create_user method in the models file of user app
        return User.objects.create_user(**validated_data)
