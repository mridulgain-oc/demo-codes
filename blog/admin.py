from datetime import date
from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    prepopulated_fields = {'slug': ("title", )}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # raw_id_fields = ('author',)
