import django_filters
from django_filters import CharFilter
from .models import tasks
class TaskFilter(django_filters.FilterSet):
    task_name = CharFilter(field_name='task_name'
                                      '', lookup_expr='icontains')
    class Meta:
        model = tasks
        fields = ['doer']
        exclude = ['task_name']