from django.contrib import admin


# Register your models here.
from .models import Elder, Author, Post, New


class PostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class meta:
        model = Post
        date_hierarchy = 'update'
        fileds = (('title', 'author'), 'content')
        list_display = ('title', 'author', 'update', 'timestamp')
        list_editable = ('author',)
        list_filter = ['update']
        search_fields = ['content', 'title']

class AuthorModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("second_name",)}

class NewModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Elder)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(New, NewModelAdmin,)
