import django_filters
from .models import Review , UserProfile


class  ReviewFilter(django_filters.FilterSet):

    class Meta:
        model = Review
        fields = [ 'text', 'date',]


class  ProfileFilter(django_filters.FilterSet):

    class Meta:
        model = UserProfile
        fields = [ 'user','phone', 'city', 'country',]
