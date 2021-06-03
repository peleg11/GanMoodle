from typing import List
from django.db import models
from django.shortcuts import render,get_object_or_404,redirect
from django.urls.base import reverse_lazy
from django.utils import timezone
from events.models import Event
from users.models import GanGroup,User
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from events.forms import EventForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar
from datetime import date, datetime

class EventListView(ListView):
    model = Event
    
    def get_queryset(self):
        return Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userGroups = self.request.user.gangroups.all()   
        context['userGroups'] = userGroups
        cal = HTMLCalendar(firstweekday=6).formatmonth(datetime.now().year,datetime.now().month,withyear=True)
        context['cal'] = cal
        context['event_list'] = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return context
    
class EventDetailView(DetailView):
    model = Event

class CreateEventView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'Event_detail.html'
    form_class = EventForm
    model = Event

class EventUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'Event_detail.html'
    form_class = EventForm
    model = Event

class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    success_url = reverse_lazy('Event_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'Event_list.html'
    model = Event
    template_name='events/Event_draft_list.html'
    
    def get_queryset(self):
        return Event.objects.filter(published_date__isnull=True).order_by('created_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drafts = Event.objects.filter(published_date__isnull=True).order_by('created_date')
        context["drafts"] = drafts
        return context

@login_required
def Event_publish(request,pk):
    event = get_object_or_404(Event,pk=pk)
    event.publish()
    group= request.user.gangroups.all()
    event.sendMail(group)
    return redirect('event_detail',pk=pk)

@login_required
def Event_attend(request,pk):
    event = get_object_or_404(Event,pk=pk)
    user = request.user
    event.add_attendee(user)
    return redirect('event_detail',pk=pk)

@login_required
def Event_attend_remove(request,pk):
    event = get_object_or_404(Event,pk=pk)
    user = request.user
    event.remove_attendee(user)
    return redirect('event_detail',pk=pk)