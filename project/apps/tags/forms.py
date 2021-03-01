import re

from django import forms
from django.utils.text import slugify
from unidecode import unidecode

from apps.tags.models import Tag


def get_slug(title):
    unidecode_title = unidecode(title)
    return slugify(re.sub(r'[^a-zA-Z0-9]', '', unidecode_title))


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not get_slug(title):
            raise forms.ValidationError(f'Плохой title - "{title}"')
        return title
