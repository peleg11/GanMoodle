from django.shortcuts import render,get_object_or_404,redirect
from django.urls.base import reverse_lazy
from django.utils import timezone
from activities.models import Activity
from users.models import GanGroup
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from activities.forms import ActivityForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class ActivitiyListView(ListView):
    model = Activity

    def get_queryset(self):
        return Activity.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userGroups = self.request.user.gangroups.all()   
        context['userGroups'] = userGroups
        activityAutherGroup = Activity.objects.all()
        
        return context

class ActivityDetailView(DetailView):
    model = Activity

class CreateActivityView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'activity_detail.html'
    form_class = ActivityForm
    model = Activity

class ActivityUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'activity_detail.html'
    form_class = ActivityForm
    model = Activity

class ActivityDeleteView(LoginRequiredMixin,DeleteView):
    model = Activity
    success_url = reverse_lazy('activity_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'activity_list.html'
    model = Activity
    template_name='activities/activity_draft_list.html'
    
    def get_queryset(self):
        return Activity.objects.filter(published_date__isnull=True).order_by('created_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drafts = Activity.objects.filter(published_date__isnull=True).order_by('created_date')
        context["drafts"] = drafts
        return context


@login_required
def activity_publish(request,pk):
    activity = get_object_or_404(Activity,pk=pk)
    activity.publish()
    return redirect('activity_detail',pk=pk)
