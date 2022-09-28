from msilib.schema import ListView
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
# Create your views here.


class InicioView(TemplateView):
    template_name = "body.html"


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwars):
        return super().dispatch(request, *args, **kwars)

    def post(self, request, *args, **kwargs):
        data = {"name":"Leonfio"}
        return JsonResponse(data)

# Controla el QuerySet del modelo, y podemos determinar el filtro a aplicar
    def get_queryset(self):
        return Category.objects.filter(name__startswith='l')

#Sobreescribimos la informacion del contexto que se envia.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context