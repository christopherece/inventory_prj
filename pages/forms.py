from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('stock_room','notes','is_available','allocated_to')