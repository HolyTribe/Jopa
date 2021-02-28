from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.text import slugify

from apps.tags.forms import TagCreateForm
from apps.tags.models import Tag
from unidecode import unidecode

MAX_ATTEMPTS_TO_CREATE = 2


class TagCreateView(TemplateView):
    template_name = 'tags/tag_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TagCreateForm()
        return context

    def post(self, *args, **kwargs):
        form = TagCreateForm(self.request.POST)

        if form.is_valid():
            if Tag.objects.filter(slug=form.cleaned_data.get('slug')).exists():
                tag = Tag.objects.filter(slug=form.cleaned_data.get('slug'))[0]
                tag.users.add(self.request.user)
                if tag.users.count() >= MAX_ATTEMPTS_TO_CREATE:
                    tag.active = True
                    tag.save()
            else:
                tag = form.save()
                tag.users.add(self.request.user)
                unidecode_title = unidecode(tag.title)
                tag.slug = slugify(unidecode_title)
                tag.save()
            return redirect(reverse('tag_create'))
        else:
            return render(self.request, 'tags/tag_create.html', context={'form': form})
