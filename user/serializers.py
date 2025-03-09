from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        extra_fields = ['first_name', 'last_name', 'full_name', 'username', 'email']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(ProfileSerializer, self).get_field_names(declared_fields, info)
        if hasattr(self.Meta, 'extra_fields'):
            expanded_fields.extend(self.Meta.extra_fields)
        return expanded_fields
