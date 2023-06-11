from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
<<<<<<< HEAD
        fields = ['status', 'created_at']
=======
        fields = ['status', 'created_at']
>>>>>>> a9a76fa5d80b9fb6b9b78964aa2052d15a7c0ac8
