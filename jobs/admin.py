from django.contrib import admin


from .models import PostJobModel, ApplicationModel

class PostJobAdmin(admin.ModelAdmin):
    list_display = ('Job_title', 'Company', 'Job_location',)

admin.site.register(PostJobModel, PostJobAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('Job_title', 'first_name', 'last_name',)

admin.site.register(ApplicationModel, ApplicationAdmin)
