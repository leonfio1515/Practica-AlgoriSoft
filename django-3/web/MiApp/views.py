from msilib.schema import ListView
from django.views.generic import TemplateView, ListView
from .models import *
# Create your views here.


class InicioView(TemplateView):
    template_name = "body.html"


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'

# Controla el QuerySet del modelo, y podemos determinar el filtro a aplicar
    def get_queryset(self):
        return Category.objects.filter(name__startswith='l')

#Sobreescribimos la informacion del contexto que se envia.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context