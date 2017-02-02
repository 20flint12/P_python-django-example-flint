from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from engine.forms import PlaceForm, ToDoForm
from engine.models import Place


class NewPlaceView(LoginRequiredMixin, CreateView):
    template_name = 'engine/edit_place.html'
    form_class = PlaceForm

    # # add the request to the kwargs
    # def get_form_kwargs(self):
    #     kwargs = super(NewPlaceView, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs

    def get_success_url(self):
        return reverse_lazy('edit_place',
                            kwargs={'place_id': self.object.id})

    # def form_valid(self, form):
    #     form.instance.user_id = self.request.user.id
    #     form.instance.edit_version = True
    #     return super(NewStudyModuleView, self).form_valid(form)


class PlaceEditView(LoginRequiredMixin, UpdateView):
    template_name = 'engine/edit_place.html'
    queryset = Place.objects
    form_class = PlaceForm

    def get_object(self, **kwargs):
        place = Place.objects.get(pk=self.kwargs['place_id'])
        return place

    # def post(self, request, *args, **kwargs):
    #
    #     return super(PlaceEditView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        place_id = self.kwargs['place_id']
        return reverse_lazy('edit_place', kwargs={'place_id': place_id})


class MomentView(FormView):
    template_name = 'engine/edit_time.html'
    # queryset = Place.objects
    form_class = ToDoForm

    def get_success_url(self):
        place_id = 1
        return reverse_lazy('edit_moment', kwargs={'place_id': place_id})
