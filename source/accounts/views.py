from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView, DetailView
from accounts.models import Profile
from accounts.forms import NewUserForm, UserEditForm
from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect


def logout_view(request):
    logout(request)
    return redirect('feed')

class UserRegisterView(CreateView):
    model = Profile
    template_name = 'accounts/sign_up.html'
    form_class = NewUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('feed'))
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('feed')
        return next_url
    
class UserProfile(DetailView):
    template_name = 'accounts/profile_page.html'
    model = Profile
    context_object_name = 'profile_obj'
    pk_url_kwarg = 'profile_pk'

def subscribe_view(request, profile_pk):
    profile_obj = Profile.objects.get(id=request.POST.get('profile_id'))
    if request.user.subs.filter(id=profile_obj.id).exists():
        request.user.subs.remove(profile_obj)
    else:
        request.user.subs.add(profile_obj)
    print(request.POST)
    return HttpResponseRedirect(reverse('accounts:profile', args=[str(profile_pk)]))