from apps.pages.models import Page
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for page, title in Page.TemplateChoice.choices:
            if page:
                Page.objects.get_or_create(template=page, title=title)
