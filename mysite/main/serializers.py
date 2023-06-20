from rest_framework import serializers
from .models import Crosses


class CrossSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crosses
        exclude = "description price".split()


class CrossDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crosses
        fields = "__all__"


class AnonymousRatingSerializer(serializers.Serializer):
    rating = serializers.FloatField(required=True, min_value=1)
    crosses_id = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=512, required=False)