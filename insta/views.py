from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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

def comment(request,image_id):
    current_user=request.user
    image = Post.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()

            print(comments)


        return redirect('index')

    else:
        form = CommentForm()

    return render(request, 'posts/comment.html', locals())

def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request,'posts/results.html',locals())

    return redirect('index')