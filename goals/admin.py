from django.contrib import admin

from .models import GoalList

from .models import GoalItem

# Register your models here.


admin.site.register(GoalList)

admin.site.register(GoalItem)
