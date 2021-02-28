import re

from django import forms

from apps.tags.models import Tag
from django.utils.text import slugify
from unidecode import unidecode


def get_slug(title):
    unidecode_title = unidecode(title)
    return slugify(re.sub(r'\s|[^a-zA-Z]', '', unidecode_title))


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title']

    def clean_title(self):
        if not get_slug(self.cleaned_data.get('title')):
            raise forms.ValidationError(f'Плохой title - "{self.cleaned_data.get("title")}"')
