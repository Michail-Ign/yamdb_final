from api.models import Genre

from rest_framework import serializers, validators


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(validators=[validators.UniqueValidator(
        queryset=Genre.objects.all())])

    class Meta:
        model = Genre
        exclude = ('id',)
