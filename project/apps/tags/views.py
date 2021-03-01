from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.tags.forms import TagCreateForm, get_slug
from apps.tags.models import Tag

MAX_ATTEMPTS_TO_CREATE = 2


class TagCreateView(FormView):
    template_name = 'tags/tag_create.html'
    form_class = TagCreateForm
    success_url = reverse_lazy('tags:create')

    def form_valid(self, form):
        slug = get_slug(form.cleaned_data.get('title'))
        tag = Tag.objects.filter(slug=slug).first()
        if tag:
            tag.users.add(self.request.user)
            if tag.users.count() >= MAX_ATTEMPTS_TO_CREATE:
                tag.active = True
                tag.save(update_fields=['active'])
        else:
            tag = form.save(commit=False)
            tag.slug = slug
            tag.save()
            tag.users.add(self.request.user)
        return super().form_valid(form)
