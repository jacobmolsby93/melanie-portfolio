from django import forms
from .models import Image, PaintingImage


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'

class PaintImageForm(forms.ModelForm):

    class Meta:
        model = PaintingImage
        fields = '__all__'
