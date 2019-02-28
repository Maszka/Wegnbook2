from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView

from .models import Wegan


class AuthorCreate(CreateView):
    model = Wegan
    fields = ['name', 'weight', 'height', 'sex', 'tags']
    template_name = 'add.html'

    def form_valid(self, form):
        print("------------")
        print(str(form))
        form.save()
        return super(AuthorCreate, self).form_valid(form)

    def get_success_url(self):
        return "../success"


class AuthorUpdate(UpdateView):
    model = Wegan
    fields = ['name', 'weight', 'height', 'sex', 'tags']

    template_name = 'add.html'


def list_of_wegans(request)
    template = loader.get_template('list.html')
    return HttpResponse(template.render({}, request))


def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render({}, request))
