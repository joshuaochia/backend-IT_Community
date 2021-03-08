from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView, DetailView,
                                  ListView, RedirectView,
                                  DeleteView, UpdateView
                                  )

from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.


class GroupCreateView(LoginRequiredMixin, CreateView):
    """ Creating new group """

    model = models.Group
    template_name = 'group_create.html'
    form_class = forms.GroupCreateForm

    def form_valid(self, form):
        form.save()
        form.instance.admin.add(self.request.user)
        form.instance.members.add(self.request.user)
        form.save()

        return super().form_valid(form)


class GroupDetailView(LoginRequiredMixin, DetailView):

    """ Group details and Post """
    model = models.Group
    template_name = 'group_detail.html'


class GroupListView(ListView):
    """ Listing available groups """

    model = models.Group
    context_object_name = 'groups'
    template_name = 'group_list.html'


class GroupJoinView(LoginRequiredMixin, RedirectView):
    """ View for leaving a group and reversing the templated on join group"""

    def get_redirect_url(self, *args, **kwargs):

        return reverse(
            'groups:group_detail',
            kwargs={'slug': self.kwargs.get('slug')}
            )

    def get(self, request, *args, **kwargs):

        group = get_object_or_404(
                models.Group,
                slug=self.kwargs.get('slug')
                )
        group.members.add(self.request.user)

        return super().get(request, *args, **kwargs)


class GroupLeaveView(LoginRequiredMixin, RedirectView):

    """ View for leaving a group"""

    def get_redirect_url(self, *args, **kwargs):
        return reverse(
            'groups:group_detail',
            kwargs={'slug': self.kwargs.get('slug')}
            )

    def get(self, request, *args, **kwargs):

        group = get_object_or_404(models.Group, slug=self.kwargs.get('slug'))
        group.members.remove(self.request.user)

        return super().get(request, *args, **kwargs)


@login_required
def group_create_post(request, slug, **kwargs):

    group = get_object_or_404(models.Group, slug=slug)

    if request.method == 'POST':
        model = models.GroupPost()
        model.body = request.POST['post-text']
        model.groups = group
        model.user = request.user
        model.save()

        return HttpResponseRedirect(
            reverse('groups:group_detail', kwargs={'slug': group.slug})
            )


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Group
    template_name = 'group_delete.html'
    success_url = reverse_lazy('groups:group_page')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.GroupPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('groups:group_page')


class PostEditView(LoginRequiredMixin, UpdateView):
    model = models.GroupPost
    template_name = 'post_edit.html'
    fields = ['body', ]
