from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, LikeView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('like/<int:pk>', LikeView, name='like_post'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r'new_comment/(\d+)/$' ,views.add_comment,name='newComment'),
    url('comment/(\d+)/$' ,views.comments,name='comments'),
    path('search/', views.search_user, name='search_results'),
      
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)