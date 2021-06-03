from django.urls import path
from events import views

urlpatterns = [
    path('',views.EventListView.as_view(),name='events_list'),
    path('event/<int:pk>',views.EventDetailView.as_view(),name='event_detail'),
    path('event/new',views.CreateEventView.as_view(),name='event_new'),
    path('event/<int:pk>/edit',views.EventUpdateView.as_view(),name='event_edit'),
    path('event/<int:pk>/delete',views.EventDeleteView.as_view(),name='event_delete'),
    path('drafts/',views.DraftListView.as_view(),name='event_draft_list'),
    path('event/<int:pk>/publish/',views.Event_publish,name='event_publish'),
    path('event/<int:pk>/attend/',views.Event_attend,name='event_attend'),
    path('event/<int:pk>/attend_remove/',views.Event_attend_remove,name='event_attend_remove'),

]
