from api.models import Category

from rest_framework import serializers, validators


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(validators=[validators.UniqueValidator(
        queryset=Category.objects.all())])

    class Meta:
        model = Category
        exclude = ('id',)
