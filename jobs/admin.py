from django.contrib import admin


from .models import PostJobModel

class PostJobAdmin(admin.ModelAdmin):
    list_display = ('Job_title', 'Company', 'Job_location',)

admin.site.register(PostJobModel, PostJobAdmin)
