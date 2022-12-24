from django import forms
from django.forms import widgets
from .models import Artikel

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('nama_tempat', 'body', 'lokasi', 'kategory')
        widgets = {
            "nama_tempat" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placholder':"Nama Tempat",
                    'required':True
                }),
            "body" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'30',
                    'rows':'10',
                    'required':True
                }),
            "lokasi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'30',
                    'rows':'10',
                    'required':True
                }),
            "kategory" : forms.Select(
                attrs={
                    'class': 'form-control selectpicker',
                    'type':'text',
                    'required':True,
                    'data-style': 'btn btn-danger btn-block',
                    'title': 'Pilih Kategory',
                    'data-size': '7'
                }),
        }