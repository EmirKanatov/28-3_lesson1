from rest_framework import serializers
from .models import Crosses, Factory, AnonymousReview


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnonymousReview
        fields = (
            'title',
            'description',
            'rating',
        )


class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = "__all__"


class CrossSerializer(serializers.ModelSerializer):
    factory = FactorySerializer()

    class Meta:
        model = Crosses
        fields = "id title get_factory_name factory description price".split()


class CrossDetailSerializer(serializers.ModelSerializer):
    factory = FactorySerializer()
    get_all_review = ReviewSerializer(many=True)

    class Meta:
        model = Crosses
        fields = "id title get_factory_name factory get_all_review description price".split()


class AnonymousRatingSerializer(serializers.Serializer):
    rating = serializers.FloatField(required=True, min_value=1)
    crosses_id = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=512, required=False)


class FactoryCreateUpdateSerializer(serializers.Serializer):
    country = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Factory.objects.create(**validated_data)