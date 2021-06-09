from api.mixins import CreateListDeleteViewSet

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from ..models.category import Category
from ..models.genre import Genre
from ..permission import AdminRequired, ReadOnly
from ..serializers.category import CategorySerializer
from ..serializers.genre import GenreSerializer


class CategoryViewSet(CreateListDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [ReadOnly | AdminRequired]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    pagination_class = PageNumberPagination


class GenreViewSet(CreateListDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [ReadOnly | AdminRequired]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    pagination_class = PageNumberPagination
