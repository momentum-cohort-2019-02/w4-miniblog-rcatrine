from django.contrib import admin
from catalog.models import Author, Blog, BlogInstance

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',)
    fields = ['first_name', 'last_name',]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BlogInstanceInline(admin.TabularInline):
    model = BlogInstance
# Register the Admin classes for Blog using the decorator
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    inlines = [BlogInstanceInline]


# Register the Admin classes for BlogInstance using the decorator
@admin.register(BlogInstance) 
class BlogInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status',)

    fieldsets = (
        (None, {
            'fields': ('imprint', 'id',)
        }),
        ('Availability', {
            'fields': ('status',)
        }),
    )
