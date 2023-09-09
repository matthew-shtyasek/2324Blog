from django.contrib import admin

# Register your models here.
from hamster.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['name', 'author', 'create_date', 'change_date']
    readonly_fields = ['create_date', 'change_date']
    search_fields = ['name', 'text']
    list_filter = ['categories', 'create_date', 'change_date']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = []
    search_fields = ['name']
