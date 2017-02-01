from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from engine.forms import PlaceForm, ToDoForm
from engine.models import Place


class PlaceEditView(LoginRequiredMixin, UpdateView):
    template_name = 'engine/edit_place.html'
    queryset = Place.objects
    form_class = PlaceForm

    def get_object(self, **kwargs):
        # if self.mymodule.frozen_at:
        #     self.mymodule = self.mymodule.save(force_clone=True)
        return Place.objects.all().first()

    # def post(self, request, *args, **kwargs):
    #     self.object = self.mymodule
    #     # TODO : check if we edit latest version
    #     # if not raise Exception()
    #
    #     return super(ModuleEditView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        place_id = 1
        return reverse_lazy('edit_place', kwargs={'place_id': place_id})


class Place2EditView(FormView):
    template_name = 'engine/edit_time.html'
    # queryset = Place.objects
    form_class = ToDoForm

    def get_success_url(self):
        place_id = 1
        return reverse_lazy('edit_moment', kwargs={'place_id': place_id})
