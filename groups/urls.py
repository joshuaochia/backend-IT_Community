from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path(
        '',
        views.GroupListView.as_view(),
        name='group_page'),
    path(
        'create/',
        views.GroupCreateView.as_view(),
        name='group_create'
        ),
    path(
        '<slug>/',
        views.GroupDetailView.as_view(),
        name='group_detail'
        ),
    path(
        '<slug>/add-post',
        views.group_create_post,
        name='group_post_create'
        ),
    path(
        '<slug>/join',
        views.GroupJoinView.as_view(),
        name='group_join'
        ),
    path(
        '<slug>/leave',
        views.GroupLeaveView.as_view(),
        name='group_leave'
        ),
    path(
        '<slug>/delete',
        views.GroupDeleteView.as_view(),
        name='group_delete'),
    path(
        'post/<int:pk>/delete/',
        views.PostDeleteView.as_view(),
        name='post_delete'
        ),
    path(
        'post/<int:pk>/update',
        views.PostEditView.as_view(),
        name='post_edit',
    )
]
