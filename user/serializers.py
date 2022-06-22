from rest_framework import serializers
from user.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = UserProfile
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    class Meta:
        # serializer에 사용될 model, field지정
        model = User
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"
