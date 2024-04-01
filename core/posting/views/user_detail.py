from django.views import generic
from ..models import User

class UserDetail(generic.DetailView):
    model = User
    template_name = 'teste.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        return context