from django import forms
from web.models import *

class MainForm(forms.Form):
    artista_selector = forms.ModelChoiceField(queryset=Artist.objects.all().order_by('name'), to_field_name='artistid',label="Artista", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="Todos")
    album_selector = forms.ModelChoiceField(queryset=Album.objects.all().order_by('title'), to_field_name='albumid',label="Album", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="Todos")
    
    