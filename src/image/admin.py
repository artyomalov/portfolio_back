from django.contrib import admin
from .models import ProjectModel, ImageModel, PreviewModel


class PreviewModelAdmin(admin.ModelAdmin):
    pass


class ImageModelAdmin(admin.ModelAdmin):
    pass


class ImageModelInline(admin.StackedInline):
    model = ImageModel
    max_num = 20
    extra = 3


class PreviewModelInline(admin.StackedInline):
    model = PreviewModel
    max_num = 1
    extra = 1


class ProjectModelAdmin(admin.ModelAdmin):
    inlines = [ImageModelInline, PreviewModelInline]


admin.site.register(ImageModel, ImageModelAdmin)
admin.site.register(ProjectModel, ProjectModelAdmin)

admin.site.register(PreviewModel, PreviewModelAdmin)
