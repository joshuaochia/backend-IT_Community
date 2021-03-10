from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path(
        '',
        views.homeview,
        name='home_page'),
    path(
        'resources/',
        views.ResourcePage.as_view(),
        name='resources_page'),
    path(
        'blog/',
        views.BlogPage.as_view(),
        name='blog_page'),
    path(
        'blog/<slug>/',
        views.BlogDetailView.as_view(),
        name='blog_detail'
        ),
    path(
        'blog/create',
        views.BlogCreateView.as_view(),
        name='blog_create'
        ),
    path(
        'blog/<slug>/update',
        views.BlogEditView.as_view(),
        name='blog_edit'
        ),
    path(
        'blog/<slug>/delete',
        views.BlogDeleteView.as_view(),
        name='blog_delete'
        ),
    path(
        '<str:slug>',
        views.ProfileView.as_view(),
        name='profile_view'
    ),
    path(
        '<str:slug>/edit',
        views.ProfileEdit.as_view(),
        name='profile_edit',
    ),
    path(
        'topic/<str:slug>',
        views.filterview,
        name='topic'
    )

]
