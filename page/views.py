from unicodedata import category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.template import context
from django.views.generic import (
                                 TemplateView, ListView, DetailView,
                                 CreateView, DeleteView, UpdateView,
                                 )
from .models import Blog
from page.forms import BlogCreateForm, ProfileUpdateForm
from django.urls import reverse, reverse_lazy
from groups.models import GroupPost, Category
from core.models import Profile
from django.db.models import Count


from django.contrib.auth import get_user_model

User = get_user_model()





class HomePage(TemplateView):
    """ Home page of website-listing post from joined groups"""

    template_name = 'index.html'


class ResourcePage(TemplateView):
    template_name = 'resources.html'


class BlogPage(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()
        return context


    def get_object(self):
        return get_object_or_404(Profile, slug=self.kwargs.get('slug'))


class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request, slug, **kwargs):
    qs = GroupPost.objects.all()
    categories = Category.objects.all()
    category = str(slug)
 
   
    qs = qs.filter(categories__name=category)


    return qs

def homeview(request, slug=None):
      

    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'index.html', context)


def filterview(request, slug):

    qs = filter(request, slug)
    


    context = {
        'queryset':qs,
        'categories': Category.objects.all()
    }

    return render(request, 'topics.html', context )





    