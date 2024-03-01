import django_filters
from .models import Task
class TaskFilter(django_filters.FilterSet):
    task_name = django_filters.CharFilter(lookup_expr='icontains', label='task_name')
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['task_name']
