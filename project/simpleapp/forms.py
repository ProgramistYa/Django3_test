from django import forms
from django.core.exceptions import ValidationError

from .models import Product

#создаем собственные проверки
class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=15)
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'quantity']


#выевление ошибки в полях
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data