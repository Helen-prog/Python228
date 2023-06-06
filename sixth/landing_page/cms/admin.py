from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe


class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    readonly_fields = ('get_img',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')

    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f"<img src='{obj.cms_img.url}' width='80'>")
        else:
            return 'нет изображения'

    get_img.short_description = 'Миниатюра'




admin.site.register(CmsSlider, CmsAdmin)

