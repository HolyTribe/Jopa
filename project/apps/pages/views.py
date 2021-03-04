from apps.commons.models import ImageModel
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import ProcessFormView


class IndexView(ProcessFormView, TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        response = {}
        if request.is_ajax():
            images = []
            for image in ImageModel.objects.iterator():
                images += [{'url': image.image.url, 'alt': image.alt, 'height': image.image.height,
                            'width': image.image.width}]
            response['images'] = images
        return JsonResponse(response)
