from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'descirption', 'price', 'Image', 'is_sold',)
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'descirption': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'Image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'name', 'descirption', 'price', 'Image',)
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'descirption': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'Image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }
 