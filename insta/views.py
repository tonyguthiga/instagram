from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Likes

from .forms import CommentForm
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts':posts})

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'posts'
    ordering = ['-created_date']
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post 
    template_name = 'posts/post_form.html'
    context_object_name = 'posts'
    fields = ['image','caption']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post 
    template_name = 'posts/post_form.html'
    context_object_name = 'posts'
    fields = ['image','caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    context_object_name = 'posts'
    fields = ['image','caption']
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def like(request, image_id):
    current_user = request.user
    image = Post.objects.get(id=image_id)
    new_like,created = Likes.objects.get_or_create(liker=current_user, image=image)
    new_like.save()

    return redirect('index')

def comments(request,id):
    comments = Comment.get_comments(id)
    return render(request,'posts/comment.html',{"comments":comments})

@login_required (login_url='/accounts/register/')
def add_comment(request,id):
   current_user = request.user
   image = Post.get_single_photo(id=id)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       print(form)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.user = current_user
           comment.image_id = id
           comment.save()
       return redirect('index')
   else:
       form = CommentForm()
       return render(request,'posts/new_comment.html',{"form":form,"image":image})
 

def search_user(request):
    name = 'Search'
    authors = Post.objects.all()
    if 'author' in request.GET and request.GET['author']:
        search_term = request.GET.get('author')
        results = Post.search_by_author(search_term)
        message = f"{search_term}"
        
        return render(request, '/posts/results.html', {'name':name, 'authors':results, 'message':message, 'authors':authors})
    else:
        message = 'You havent searched yet'
        return render(request, 'posts/results.html',{'message':message})