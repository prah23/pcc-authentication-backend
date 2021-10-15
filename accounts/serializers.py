from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ImageSerializerField(serializers.Field):

    def to_representation(self, obj):
        return self.context['request'].build_absolute_uri(obj.profile_picture.url)


class UserInfoSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField('_get_image_url')
    
    def _get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.profile_picture.url)

    class Meta:
        model = User
        fields = [
            'email',
            'full_name',
            'profile_picture',
            'phone_number',
            'date_of_birth',
        ]


class UserModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'full_name',
            'profile_picture',
            'phone_number',
            'date_of_birth',
        ]