from django import template

from apps.settings.models import Settings

register = template.Library()


class Seo:
    def __init__(self, context):
        self.context = context
        self.settings = Settings.objects.first()
        page = self.context.get('page')
        obj = self.context.get('obj')
        self.current = page or obj
        self.replacing = (
            ('[title]', self.settings.title),
            ('[object]', self.current.__str__()),
        )

    def clean(self, string: str) -> str:
        """Замена переменных"""
        for key, value in self.replacing:
            string = string.replace(key, value)
        return string

    def get_tag(self) -> dict:
        """Получение информации страницы
        :return: dict [title, meta_title, meta_description]"""
        response = {}
        if self.current:
            response['title'] = self.current.__str__()
            response['meta_title'] = self.clean(self.current.meta_title or self.settings.title_default)
            response['meta_description'] = self.clean(
                self.current.meta_description or self.settings.description_default)
        return response


@register.simple_tag(takes_context=True)
def get_page_info(context):
    """Получает информацию о странице"""
    return Seo(context).get_tag()
