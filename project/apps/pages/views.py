from apps.commons.models import ImageModel
from apps.pages.models import Page
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import ProcessFormView


class ContextPageMixin(TemplateView):
    """Миксин для прикрутки страницы"""
    page = None

    def get_context_data(self, **kwargs):
        context = super(ContextPageMixin, self).get_context_data(**kwargs)
        page = Page.objects.exclude(template__isnull=True).filter(template=self.page).first()
        if page:
            context['page'] = page
        return context


class IndexView(ContextPageMixin, ProcessFormView, TemplateView):
    template_name = "index.html"
    page = Page.TemplateChoice.INDEX

    def post(self, request, *args, **kwargs):
        response = {}
        if request.is_ajax():
            images = []
            for image in ImageModel.objects.iterator():
                images += [{'url': image.image.url, 'alt': image.alt, 'height': image.image.height,
                            'width': image.image.width}]
            response['images'] = images
        return JsonResponse(response)
