from django.contrib import admin
from django import forms
from guide.models import Lecturer, Course, Category, CourseComment, LecturerComment, CourseRating, LecturerRating

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'currentlecturer', 'school', 'avg_rating', 'views', 'short_description', 'short_requirements')
    list_filter = ('school',)
    exclude = ('no_comments','avg_rating', 'slug', 'category', 'views')
admin.site.register(Course, CourseAdmin)

class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'teaching', 'avg_rating', 'views', 'short_description')
    exclude = ('no_comments','avg_rating', 'slug', 'category', 'views')
admin.site.register(Lecturer, LecturerAdmin)

class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'page', 'short_comment')
    list_filter = ('page', 'user')
admin.site.register(CourseComment, CourseCommentAdmin)

class LecturerCommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'page', 'short_comment')
    list_filter = ('page', 'user')
admin.site.register(LecturerComment, LecturerCommentAdmin)

class LecturerRatingAdmin(admin.ModelAdmin):
    list_display = ('date', 'page', 'user', 'rating')
    list_filter = ('page', 'user', 'rating')
admin.site.register(LecturerRating, LecturerRatingAdmin)

class CourseRatingAdmin(admin.ModelAdmin):
    list_display = ('date', 'page', 'user', 'rating')
    list_filter = ('page', 'user', 'rating')
admin.site.register(CourseRating, CourseRatingAdmin)

