from django.contrib import admin
from .models import Data
from .models import userInfo
from .models import tasks
from .models import Tag

# Register your models here.
admin.site.register(Data)
admin.site.register(userInfo)
admin.site.register(tasks)
admin.site.register(Tag)


#username = asadbek
#password: asad1234