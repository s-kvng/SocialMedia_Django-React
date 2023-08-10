from rest_framework import serializers

from core.user.models import User
from core.abstract.serializers import AbstractSerializer


# serializers.ModelSerializer is a class inheriting from the serializers.Serializer class
class UserSerializer(serializers.ModelSerializer, AbstractSerializer):
    # It’ll automatically match the field of the model to have the correct validations for each one.
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "email",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_field = ["is_active"]
