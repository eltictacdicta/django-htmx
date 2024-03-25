from django.test import SimpleTestCase
from django.urls import reverse



class HomePageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('bases:home')
        self.response = self.client.get(url)

    def test_url_home(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_home(self):
        self.assertTemplateUsed(self.response, 'bases/home.html')
        self.assertContains(self.response, '<h4 class="card-title">Success card title</h4>')
        self.assertNotContains(self.response, 'Curso de Django')
