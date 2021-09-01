from rest_framework import serializers
from .models import Description


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id', 'title', 'title_detail', 'product']


    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

