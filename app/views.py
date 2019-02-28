from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView

from .models import Wegan


class WeganCreate(CreateView):
    model = Wegan
    fields = ['name', 'weight', 'height', 'sex', 'tags']
    template_name = 'add.html'

    def form_valid(self, form):
        print("------------")
        print(str(form))
        form.save()
        return super(WeganCreate, self).form_valid(form)

    def get_success_url(self):
        return "../success"


class WeganUpdate(UpdateView):
    model = Wegan
    fields = ['name', 'weight', 'height', 'sex', 'tags']

    template_name = 'add.html'

    def form_valid(self, form):
        print("------------")
        print(str(form))
        form.save()
        return super(WeganUpdate, self).form_valid(form)

    def get_success_url(self):
        return "../success"


def list_of_wegans(request):
    template = loader.get_template('list.html')
    wegans = Wegan.objects.all()
    return HttpResponse(template.render({'wegans': wegans}, request))


def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render({}, request))
