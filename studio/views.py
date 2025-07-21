from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from studio.forms import MasterCreationForm
from studio.models import JewelryType, Jewelry, Master

@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_jewelry_types = JewelryType.objects.count()
    num_jewelry = Jewelry.objects.count()
    num_masters = Master.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_jewelry_types': num_jewelry_types,
        'num_jewelry': num_jewelry,
        'num_masters': num_masters,
        'num_visits': num_visits,
    }
    return render(request, 'studio/index.html', context)

class JewelryTypeListView(LoginRequiredMixin ,generic.ListView):
    model = JewelryType
    template_name = "studio/jewelry_type_list.html"
    context_object_name = "jewelry_type_list"


class JewelryTypeCreateView(LoginRequiredMixin ,generic.CreateView):
    model = JewelryType
    fields = "__all__"
    success_url = reverse_lazy("studio:jewelry-type-list")
    template_name = "studio/jewelry_type_form.html"


class JewelryTypeUpdateView(LoginRequiredMixin ,generic.UpdateView):
    model = JewelryType
    fields = "__all__"
    success_url = reverse_lazy("studio:jewelry-type-list")
    template_name = "studio/jewelry_type_form.html"

class JewelryTypeDeleteView(LoginRequiredMixin ,generic.DeleteView):
    model = JewelryType
    success_url = reverse_lazy("studio:jewelry-type-list")
    template_name = "studio/jewelry_type_confirm_delete.html"


class JewelryListView(LoginRequiredMixin ,generic.ListView):
    model = Jewelry
    paginate_by = 2


class JewelryDetailView(LoginRequiredMixin ,generic.DetailView):
    model = Jewelry

class JewelryCreateView(LoginRequiredMixin ,generic.CreateView):
    model = Jewelry

class JewelryUpdateView(LoginRequiredMixin ,generic.UpdateView):
    model = Jewelry


class MasterListView(LoginRequiredMixin ,generic.ListView):
    model = Master


class MasterDetailView(LoginRequiredMixin ,generic.DetailView):
    model = Master

class MasterCreateView(LoginRequiredMixin ,generic.CreateView):
    model = Master
    form_class = MasterCreationForm


