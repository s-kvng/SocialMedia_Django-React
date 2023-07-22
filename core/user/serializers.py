from rest_framework import serializers

from core.user.models import User


# serializers.ModelSerializer is a class inheriting from the serializers.Serializer class
class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="public_id", read_only=True, format="hex")
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

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
