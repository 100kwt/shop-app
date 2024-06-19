from django.contrib import admin
from .models import Course, Category

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)

