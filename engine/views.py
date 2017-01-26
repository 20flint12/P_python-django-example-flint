
from django.views.generic import View, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from engine.forms import PlaceForm
from engine.models import Place


class PlaceEditView(LoginRequiredMixin, UpdateView):
    template_name = 'engine/edit_module.html'
    queryset = Place.objects
    form_class = PlaceForm

    def get_object(self, **kwargs):
        # if self.mymodule.frozen_at:
        #     self.mymodule = self.mymodule.save(force_clone=True)
        return Place.objects.get(id=1)

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #
    #     path = reverse_lazy('edit_module', kwargs={'module_id': self.object.id})
    #     if self.request.path != path:
    #         return HttpResponseRedirect(path)
    #     else:
    #         return super(ModuleEditView, self).get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.object = self.mymodule
    #     # TODO : check if we edit latest version
    #     # if not raise Exception()
    #
    #     return super(ModuleEditView, self).post(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ModuleEditView, self).get_context_data(**kwargs)
    #     context['pages'] = ModulePage.objects.filter(module_id=self.mymodule.id)
    #     return context

    # def get_success_url(self):
    #     if self.mymodule.cloned_id > 1:
    #         module_id = self.mymodule.cloned_id
    #     else:
    #         module_id = self.mymodule.id
    #     return reverse_lazy('edit_module', kwargs={'module_id': module_id})
