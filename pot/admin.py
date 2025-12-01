from django.contrib import admin
from .models import Project, FAQ, Contact, About, Post

from .models import About


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'link', 'created_at')
	search_fields = ('title', 'description')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
	list_display = ('question', 'created_at')
	search_fields = ('question', 'answer')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
	list_filter = ('is_read', 'created_at')
	search_fields = ('name', 'email', 'message', 'subject')
	actions = ['mark_read', 'mark_unread']

	def mark_read(self, request, queryset):
		queryset.update(is_read=True)
		self.message_user(request, "Selected messages marked as read.")
	mark_read.short_description = "Mark selected messages as read"

	def mark_unread(self, request, queryset):
		queryset.update(is_read=False)
		self.message_user(request, "Selected messages marked as unread.")
	mark_unread.short_description = "Mark selected messages as unread"
    
	# show budget in admin list
	list_display = ('name', 'email', 'subject', 'budget', 'created_at', 'is_read')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	list_display = ('name', 'tagline')
	readonly_fields = ()
	search_fields = ('name', 'tagline', 'bio')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'published', 'published_at', 'created_at')
	list_filter = ('published', 'published_at')
	search_fields = ('title', 'excerpt', 'content')
	prepopulated_fields = {'slug': ('title',)}
