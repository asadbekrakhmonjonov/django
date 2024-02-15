from django.forms import ModelForm
from .models import Data
from .models import tasks
class registerForm(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
class taskForm(ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'
