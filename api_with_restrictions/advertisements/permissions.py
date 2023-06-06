from rest_framework.permissions import BasePermission, SAFE_METHODS

from advertisements.models import Advertisement, AdvertisementStatusChoices


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if Advertisement.objects.filter(creator=user, status=AdvertisementStatusChoices.OPEN).count() >= 10:
            return False
        return True