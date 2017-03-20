from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_disply = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_field = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
