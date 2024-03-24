from django.test import SimpleTestCase
from django.urls import reverse



class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('pages:about')
        self.response = self.client.get(url)

    def test_url_about(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_about(self):
        self.assertTemplateUsed(self.response, 'paginas/about.html')
        self.assertContains(self.response, '<h1>Sobre mi</h1>')
        self.assertNotContains(self.response, 'Curso de Django')



    '''def test_existe_ruta(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)

    def test_nombre_ruta_about(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)


    def test_plantilla_contiene_html_correcto(self):
        response = self.client.get(reverse('pages:about'))
        self.assertContains(response, '<h1>Sobre mi</h1>')

    def test_plantilla_no_contiene_html_correcto(self):
        response = self.client.get(reverse('pages:about'))
        self.assertNotContains(response, 'Curso de Django')

    def test_about_page_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/about/')
        self.assertContains(response, '<h1>About Page</h1>')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/about/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_about_page_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, 'AboutPageView'''