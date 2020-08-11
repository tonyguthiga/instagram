from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', PostListView.as_view(), name='index'),
    url('post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('post/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
    url('post/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^search/',views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)