from django.contrib import admin
from guide.models import Lecturer, Course, Category, CourseComment, LecturerComment, CourseRating, LecturerRating 
# Register your models here.

admin.site.register(Category)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'currentlecturer', 'school', 'views')
admin.site.register(Course, CourseAdmin)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'teaching', 'views')
admin.site.register(Lecturer, LecturerAdmin)

class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'page')
admin.site.register(CourseComment, CourseCommentAdmin)

class LecturerCommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'page')
admin.site.register(LecturerComment, LecturerCommentAdmin)

class LecturerRatingAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'page')
admin.site.register(LecturerRating, LecturerRatingAdmin)

class CourseRatingAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'page')
admin.site.register(CourseRating, CourseRatingAdmin)