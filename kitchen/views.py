from django.views.generic import TemplateView
from kitchen.models import Drink
# Create your views here.
class PizzaListView(TemplateView):
    template_name = 'pizzaa.html '


class DrinkListView(TemplateView):
    template_name = 'hoho.html'
    def get_context_data(self, **kwargs):
        context = dict()
        drink = Drink.ob