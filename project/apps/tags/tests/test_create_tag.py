from django.test import TestCase, Client
from django.urls import reverse

from apps.tags.models import Tag
from apps.users.models import User
from apps.tags.views import MAX_ATTEMPTS_TO_CREATE


CORRECT_TAG_TITLE = ' Ми1нима2лист3ичная  4  жи5вопись --66 !! 7~~ Ё kr9yta!8!! с0уп_ер бомба. Ставлю класс'
CORRECT_TAG_SLUG = 'mi1nima2list3ichnaia4zhi5vopis667iokr9yta8s0uperbombastavliuklass'

INCORRECT_TAG_TITLE = '- - __ !!! ~~'

SOME_USERS_CRATE_TAG_TITLE = 'Современная живопись'

USER_NAME = 'test_user'
USER_PASSWORD = 'pass@123'
USER_EMAIL = 'admin@mail.ru'

# TODO: Написать проверку на создание несколькими пользователями тегов


class CreateTagTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for i in range(MAX_ATTEMPTS_TO_CREATE):
            User.objects.create_user(username=str(i)+USER_NAME, email=str(i)+USER_EMAIL, password=USER_PASSWORD)

    def test_200_response_tag_create_page(self):
        """Проверка на 200 ответ страницы создания
            УДАЛИТЬ ЭТУ ПРОВЕРКУ ПОЗЖЕ!!!
        """
        url = reverse('tags:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_correct_tag(self):
        """Проверка корректоного тайтла. slug тега должен быть равен CORRECT_TAG_SLUG"""

        client = Client()
        client.login(password=USER_PASSWORD, username='0'+USER_NAME)
        client.post(reverse('tags:create'), {'title': CORRECT_TAG_TITLE})

        tag = Tag.objects.first()
        self.assertEqual(tag.slug, CORRECT_TAG_SLUG)

    def test_create_incorrect_tag(self):
        """Проверка некорректного тайтла. Не должно создаться тегов. И должна быть ошибка в форме"""

        client = Client()
        client.login(password=USER_PASSWORD, username=USER_NAME)
        response = client.post(reverse('tags:create'), {'title': INCORRECT_TAG_TITLE})

        tags_count = Tag.objects.all().count()
        self.assertEqual(tags_count, 0)

        title_error = response.context_data.get('form').has_error('title')
        self.assertEqual(title_error, True)

    def test_another_user_create_tag(self):
        """Проверка на создание 1 тега уже другим пользователем"""

        old_tags_count = Tag.objects.count()
        for i in range(MAX_ATTEMPTS_TO_CREATE):

            client = Client()
            client.login(password=USER_PASSWORD, username=str(i)+USER_NAME)
            client.post(reverse('tags:create'), {'title': SOME_USERS_CRATE_TAG_TITLE})

            self.assertEqual(Tag.objects.count(), old_tags_count + 1)

            tag = Tag.objects.filter(title=SOME_USERS_CRATE_TAG_TITLE).first()

            # -1 потому что i начинаеться с 0
            if i >= MAX_ATTEMPTS_TO_CREATE - 1:
                self.assertTrue(tag.active)
            else:
                self.assertFalse(tag.active)
