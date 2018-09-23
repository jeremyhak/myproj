from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,password_reset_complete


app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$',views.signup_view, name="signup"),
    url(r'^login/$',views.login_view, name="login"),
    url(r'^logout/$',views.logout_view, name="logout"),
    url(r'^profile/$',views.profile_view, name="profile"),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_view, name='view_profile_with_pk'),
    #url(r'^profile/edit/$',views.edit_user, name="edit_profile"),
    url(r'^my-profile/$',views.my_profile_view, name="my-profile"),
    url(r'^my-profile/(?P<pk>\d+)/$', views.my_profile_view, name='view_my-profile_with_pk'),
    #url(r'^profile/create-review/$',views.reviews_create, name="create-review"),
    #url(r'^profile/reviews/$',views.reviews, name="reviews"),
    #url(r'^my-profil/reviews/$', views.reviews, name='reviews_with_pk'),
    url(r'^my-profile/update/$', views.edit_user, name='account_update'),

    url(r'^my-profile/photo-update/$', views.edit_photo, name='photo_update'),
    url(r'^change-password/$',views.change_password_view, name="change_password"),
    url(r'^reset-password/$', password_reset , name="password_reset"),
    url(r'^reset-password/done/$', password_reset_done, name="password_reset_done"),
    url(r'^reset-password/confirm/$(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
     password_reset_confirm, name="password_reset_confirm"),
    url(r'^reset-password/complete/$', password_reset_complete, name="password_reset_complete"),


]
