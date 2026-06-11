from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    age = serializers.IntegerField(min_value=0)