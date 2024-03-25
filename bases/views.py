from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def primera_vista(request):
    return HttpResponse("Hola Mundo")


class HomeView(TemplateView):
    template_name = 'bases/home.html'

    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Mi primera página con Django'
        return context """