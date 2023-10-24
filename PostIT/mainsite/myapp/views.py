from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
from .models import Post
from .forms import PostForm

def create_posts(request):
    return render(request, 'create_posts.html')

class PostList(LoginRequiredMixin, ListView):
    template_name = 'post_list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.all()
        return context
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts_list')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts_list')
        return super(RegisterPage, self).get(*args, **kwargs)

@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)
    posts_count = posts.count()
    return render(request, 'account.html', {'posts_count':posts_count})

class MyPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'my_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['my_posts'] = Post.objects.filter(author=self.request.user)
        return context
    
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_form2.html'
    form_class = PostForm
    success_url = reverse_lazy('posts_list')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts_list')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(author = owner)