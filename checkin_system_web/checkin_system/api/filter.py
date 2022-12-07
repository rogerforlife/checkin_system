import django_filters
from checkin_system.models import Checkindata, Hrdata


class HrdataFilter(django_filters.FilterSet):
    supervisor_id = django_filters.CharFilter(
        field_name='supervisor_id', lookup_expr='icontains')
    department_id = django_filters.CharFilter(
        field_name='department_id', lookup_expr='icontains')

    class Meta:
        model = Hrdata
        fields = ['supervisor_id', 'department_id']


class CheckindataFilter(django_filters.FilterSet):
    employee_id = django_filters.CharFilter(
        field_name='employee_id', lookup_expr='icontains')

    class Meta:
        model = Checkindata
        fields = ['employee_id', 'checkin_date']
