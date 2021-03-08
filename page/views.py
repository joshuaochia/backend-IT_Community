from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import (
                                 TemplateView, ListView, DetailView,
                                 CreateView, DeleteView, UpdateView,
                                 )
from .models import Blog
from page.forms import BlogCreateForm
from django.urls import reverse, reverse_lazy
from groups.models import GroupPost
from core import models
from django.contrib.auth import get_user_model

User = get_user_model()


Profile = models.Profile


class HomePage(TemplateView):
    """ Home page of website-listing post from joined groups"""

    template_name = 'index.html'


class ResourcePage(TemplateView):
    template_name = 'resources.html'


class BlogPage(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogCreateForm
    template_name = 'blog_create.html'


class BlogEditView(LoginRequiredMixin, UpdateView):
    form_class = BlogCreateForm
    template_name = 'blog_create.html'
    model = Blog

    def get_success_url(self, **kwargs):
        return reverse('page:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('page:blog_page')


class ProfileView(LoginRequiredMixin, ListView):
    """ View for profile information and latest activity"""
    model = GroupPost
    template_name = 'profile.html'
    context_object_name = 'posts'

    def get_object(self):
        return get_object_or_404(Profile, slug=self.kwargs.get('slug'))


class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = models.Profile
    template_name = 'profile_update.html'
    fields = ['bio', ]
