from django import forms

from webshop_01.shop.models import Order


class BootsTrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class OrderForm(BootsTrapMixin, forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'description']

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                })
        }
