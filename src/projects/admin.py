from django.contrib import admin
from .models import ProjectModel, ImageModel, PreviewModel
from django import forms


class ImageFormset(forms.models.BaseInlineFormSet):
    """
    validate preview and image forms has at least one added image
    """
    def clean(self):
        # get forms that actually have valid data
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                # annoyingly, if a subform is invalid Django explicity raises
                # an AttributeError for cleaned_data
                pass
        if count < 1:
            raise forms.ValidationError('Add at least one image')




class PreviewModelAdmin(admin.ModelAdmin):
    pass


class ImageModelAdmin(admin.ModelAdmin):
    pass


class ImageModelInline(admin.StackedInline):
    model = ImageModel
    formset = ImageFormset
    max_num = 20
    extra = 3


class PreviewModelInline(admin.StackedInline):
    model = PreviewModel
    formset = ImageFormset
    max_num = 1
    extra = 1


class ProjectModelAdmin(admin.ModelAdmin):
    inlines = [ImageModelInline, PreviewModelInline]


admin.site.register(ImageModel, ImageModelAdmin)
admin.site.register(ProjectModel, ProjectModelAdmin)
admin.site.register(PreviewModel, PreviewModelAdmin)
