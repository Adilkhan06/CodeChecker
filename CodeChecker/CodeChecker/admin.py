from django.contrib import admin
from .models import admin_panel
from .models import CustomUser
from .models import FAQ
from .models import Condition, Task
from .models import Lecture

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'assignment_link')
    search_fields = ('title', 'description')


class FAQAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'question', 'answer', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user_name', 'question']


class TaskAdmin(admin.ModelAdmin):
    raw_id_fields = ['condition']


admin.site.register(CustomUser)

admin.site.register(Condition)

admin.site.register(Task, TaskAdmin)

admin.site.register(admin_panel)

admin.site.register(FAQ, FAQAdmin)


