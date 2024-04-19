from django.db.models import Count, Prefetch, Q
from rest_framework.viewsets import ReadOnlyModelViewSet

from food.models import Food, FoodCategory

from .serializers import FoodListSerializer


class FoodViewSet(ReadOnlyModelViewSet):
    """Вывод блюд, которые опубликованы."""

    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.annotate(
        num_published_foods=Count('food', filter=Q(food__is_publish=True))
    ).prefetch_related(
        Prefetch(
            'food',
            queryset=Food.objects.filter(is_publish=True),
        ),
    ).distinct()
