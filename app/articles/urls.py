from django.conf.urls import url
from . import views
from .forms import CreatePosts , PickDrop
from .views import PostCreateWizard

app_name = 'articles'

urlpatterns = [
    url(r'^$',views.article_list, name = "list"),
    url(r'^create/$',PostCreateWizard.as_view([CreatePosts, PickDrop]), name="create"),
    url(r'^(?P<id>\d+)/$', views.article_detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/$',views.article_delete, name = "delete"),
    url(r'^filter/$',views.filter, name = "filter"),
    url(r'^pickup-detail/(?P<id>\d+)/$', views.pickup_detail, name="pickupdetail"),
    url(r'^myposts/$',views.my_posts, name = "myposts"),
    #url(r'^messages/$',views.IndexView, name = "messages"),
]
