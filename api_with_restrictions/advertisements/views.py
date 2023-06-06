from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    permisson_classes = [IsOwnerOrReadOnly]

    def get_permissions(self):
        """Получение прав для действий."""
        permissions = [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions.append(IsOwnerOrReadOnly())
        return permissions

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != request.user:
            return Response(status = status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status = status.HTTP_204_NO_CONTENT)