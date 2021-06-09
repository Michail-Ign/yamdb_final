from django.db.models import Avg
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import SAFE_METHODS

from api.filters.filters import TitlesFilter
from api.models import Title
from api.permission import IsAdminOrReadOnly
from api.serializers.title import TitleDetailSerializer, TitleListSerializer


class TitelViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('review__score')).all().order_by('name')
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleListSerializer
        return TitleDetailSerializer
