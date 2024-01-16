from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from feed.forms import CommentModel, PostForm
from feed.models import PostModel
from accounts.models import Profile
from django.views.generic.edit import FormMixin, FormView
# Create your views here.


class FeedView(LoginRequiredMixin, ListView):
    login_url = 'accounts:log_in'
    template_name = 'feed.html'
    context_object_name = 'post_obj'
    model = PostModel

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

class PostCreateView(CreateView):
    template_name = 'content/new_post.html'
    form_class = PostForm
    model = PostModel

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(kwargs)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        print(form.data)
        print(form.errors)
        print(self.request.POST.dict())
        return redirect('feed')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('feed')
 

def post_like_view(request, post_pk):
    post = PostModel.objects.get(id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('feed'))



    