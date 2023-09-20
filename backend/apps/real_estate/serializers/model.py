from rest_framework import serializers

from ..models import Realestate


class RealestateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestate
        fields = "__all__"
