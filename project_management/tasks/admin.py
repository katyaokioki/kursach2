from django.contrib import admin
from .models import Project, Task, User, Assignment, Comment, Tag

# admin.site.register(Project)
# admin.site.register(Task)
# admin.site.register(User)
# admin.site.register(Assignment)
# admin.site.register(Comment)
# admin.site.register(Tag)



from django.contrib import admin
from .models import Project, Task, User, Assignment, Comment, Tag

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'user_count')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'start_date'

    @admin.display(description='Количество пользователей')
    def user_count(self, obj):
        return obj.users.count()

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'project')
    list_filter = ('project', 'due_date')
    search_fields = ('title',)
    raw_id_fields = ('project',)
    filter_horizontal = ('tags',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'created_at')
    list_filter = ('task', 'user')
    readonly_fields = ('created_at',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Assignment)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)


# from django.contrib import admin
# from .models import Project, Task, Assignment, Comment, Tag

# class CommentInline(admin.TabularInline):  # Использование inlines
#     model = Comment
#     extra = 1  # Количество пустых форм для добавления комментариев

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'start_date', 'end_date', 'user_count')  # Использование list_display
#     list_filter = ('start_date', 'end_date')  # Использование list_filter
#     inlines = [CommentInline]  # Использование inlines
#     date_hierarchy = 'start_date'  # Использование date_hierarchy
#     search_fields = ('name', 'description')  # Использование search_fields

#     @admin.display(description='User Count')  # Использование @admin.display и short_description
#     def user_count(self, obj):
#         return obj.users.count()  # Собственный метод для отображения количества пользователей

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'project', 'due_date')  # Использование list_display
#     list_filter = ('project',)  # Использование list_filter
#     raw_id_fields = ('project',)  # Использование raw_id_fields
#     readonly_fields = ('due_date',)  # Использование readonly_fields

# @admin.register(Assignment)
# class AssignmentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'task')  # Использование list_display

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name',)  # Использование list_display
