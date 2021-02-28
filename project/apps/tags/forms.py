from django import forms

from apps.tags.models import Tag


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title']
