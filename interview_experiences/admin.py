from django.contrib import admin
# Register your models here.

from .models import experience
from .models import comment

admin.site.register(experience)
admin.site.register(comment)