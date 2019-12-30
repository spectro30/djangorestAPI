from rest_framework import serializers
from .models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('key', 'val', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')