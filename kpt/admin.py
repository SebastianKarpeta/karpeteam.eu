from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category


# ------------------ POST ADMIN ------------------
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'category', 'author', 'is_active', 'create_date')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'text')

    # Skrócony tytuł z tooltipem
    def short_title(self, obj):
        if len(obj.title) > 100:
            return format_html('<span title="{}">{}...</span>', obj.title, obj.title[:100])
        return obj.title
    short_title.short_description = 'Tytuł'


# ------------------ CATEGORY ADMIN ------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'is_active', 'create_date')
    list_editable = ('is_active',)
    list_filter = ('is_active',)

    # Skrócony tytuł z tooltipem
    def short_title(self, obj):
        if len(obj.title) > 100:
            return format_html('<span title="{}">{}...</span>', obj.title, obj.title[:100])
        return obj.title
    short_title.short_description = 'Tytuł'
