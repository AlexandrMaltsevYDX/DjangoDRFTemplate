from rest_framework import serializers

from .models import CardModel


class CardModelSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField()

    class Meta:
        model = CardModel
        fields = "__all__"

