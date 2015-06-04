from django.contrib import admin

# Register your models here.
from collection.models import Post

class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ('title', 'text')
	prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)