from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView

from .models import Wegan


class AuthorCreate(CreateView):
    model = Wegan
    fields = ['name', 'weight', 'height', 'sex', 'tags']
    template_name = 'add.html'

    def get_absolute_url(self):
        return "ASD"

    def get_success_url(self):
        return "/validate"


class AuthorUpdate(UpdateView):
    model = Wegan
    fields = ['name', 'weight', 'height', 'sex', 'tags']

    template_name = 'add.html'


def validate(request):
    return HttpResponse(str(request.POST))
