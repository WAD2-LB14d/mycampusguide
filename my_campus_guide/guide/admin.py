from django.contrib import admin
from guide.models import Lecturer, Course, Category 
# Register your models here.

admin.site.register(Category)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'currentlecturer', 'school', 'views')
admin.site.register(Course, CourseAdmin)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'teaching', 'views')
admin.site.register(Lecturer, LecturerAdmin)
