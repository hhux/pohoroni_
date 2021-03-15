from PIL import Image

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class CoffinAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red;">При загрузке изображения с разрешением больше {}x{} оно будет обрезано</span>
            """.format(
                *Product.MIN_RESOLUTION
            )
        )

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     img = Image.open(image)
    #     min_height, min_width = Product.MIN_RESOLUTION
    #     max_height, max_width = Product.MAX_RESOLUTION
    #     if image.size > Product.MAX_IMAGE_SIZE:
    #         raise ValidationError('Размер файла не должен превышать 3МВ')
    #     if img.height < min_height or img.width < min_width:
    #         raise ValidationError('Разрешение изображение меньше минимального')
    #     if img.height > max_height or img.width > max_width:
    #         raise ValidationError('Разрешение изображение больше максимального')
    #     return image


class CoffinAdmin(admin.ModelAdmin):

    form = CoffinAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='coffins'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class UrnAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='urns'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class InfoAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='info'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Coffin, CoffinAdmin)
admin.site.register(Urn, UrnAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Info, InfoAdmin)

""""1"""