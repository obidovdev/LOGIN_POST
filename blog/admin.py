from django.contrib import admin

from blog.models import Post , Comments


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at','updated_at','is_active')
    ordering = ('-created_at',)

@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    list_display = ('post','created_at','updated_at','is_active')
    ordering = ('-created_at',)