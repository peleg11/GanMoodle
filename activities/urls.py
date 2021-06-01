from django.urls import path
from activities import views

urlpatterns = [
    path('',views.ActivitiyListView.as_view(),name='activity_list'),
    path('activity/<int:pk>',views.ActivityDetailView.as_view(),name='activity_detail'),
    path('activity/new',views.CreateActivityView.as_view(),name='activity_new'),
    path('activity/<int:pk>/edit',views.ActivityUpdateView.as_view(),name='activity_edit'),
    path('activity/<int:pk>/delete',views.ActivityDeleteView.as_view(),name='activity_delete'),
    path('drafts/',views.DraftListView.as_view(),name='activity_draft_list'),
    path('activity/<int:pk>/publish/',views.activity_publish,name='activity_publish'),

]
