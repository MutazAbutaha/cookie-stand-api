from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import cookie_stands


class cookie_standsListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/cookie_stands_list.html"
    model = cookie_stands
    context_object_name = "cookie_stands"


class cookie_standsDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/cookie_stands_detail.html"
    model = cookie_stands


class cookie_standsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/cookie_stands_update.html"
    model = cookie_stands
    fields = "__all__"


class cookie_standsCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/cookie_stands_create.html"
    model = cookie_stands
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class cookie_standsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/cookie_stands_delete.html"
    model = cookie_stands
    success_url = reverse_lazy("cookie_stands_list")
