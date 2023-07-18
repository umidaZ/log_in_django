from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import PostForm
from .models import Post


# Create your views here.
# CRUD => CREATE READ UPDATE DELETE
class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail_view.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    fields = '__all__'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update_post.html'
    # fields = ['title', 'body']


class PostDeleteView(generic.DetailView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')
