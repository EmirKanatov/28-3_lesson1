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


class CrossModelSerializer(serializers.ModelSerializer):
    factory = FactorySerializer()

    class Meta:
        model = Crosses
        fields = "id title get_factory_name factory description price".split()


class CrossSerializer(serializers.Serializer):
    title = serializers.CharField()
    factory_id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

    def validate_factory_id(self, factory_id):
        try:
            Factory.objects.get(id=factory_id)
        except Factory.DoesNotExist:
            raise serializers.ValidationError("Factory not found")
        return factory_id

    def validate_title(self, title):
        if Crosses.objects.filter(title=title).count() > 0:
            raise serializers.ValidationError("Crosses with this title already exists")
        return title

    def create(self, validated_data):
        cross = Crosses.objects.create(title=validated_data['title'],
                                       description=validated_data['description'],
                                       price=validated_data['price'],
                                       factory_id=validated_data['factory_id'])
        return cross

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