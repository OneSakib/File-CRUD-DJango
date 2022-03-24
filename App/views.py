from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import FormView, RedirectView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from .forms import DataForm
from .models import Data


# Create your views here.
@method_decorator(login_required(login_url=reverse_lazy('app:login'), redirect_field_name=''), name='dispatch')
class Dashboard(TemplateView):
    template_name = 'app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['form'] = DataForm()
        context['data'] = Data.objects.all()
        return context

    def post(self, request):
        if request.method == 'POST':
            form = DataForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('app:dashboard'))
            return HttpResponseRedirect(reverse_lazy('app:dashboard'))


class LoginForm(FormView):
    template_name = 'app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('app:dashboard')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(reverse_lazy('app:dashboard'))


class Logout(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect(reverse_lazy('app:login'))


class SignUpForm(FormView):
    template_name = 'app/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('app:login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('app:login'))
        return HttpResponseRedirect(reverse_lazy('app:signup'))


class UpdateData(UpdateView):
    template_name = 'app/update.html'
    form_class = DataForm
    success_url = reverse_lazy('app:dashboard')
    model = Data


class DeleteData(DeleteView):
    template_name = 'app/delete.html'
    success_url = reverse_lazy('app:dashboard')
    model = Data

