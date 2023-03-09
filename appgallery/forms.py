from tkinter import PhotoImage
from django import forms

from appgallery.models import gallery

class GalleryForm(forms.ModelForm):
    
    class Meta:
        model = gallery
        fields = ("photo",)
        labels = {'photo':''}
