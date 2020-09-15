from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^blog/create/', views.blog_create),
  url(r'^blog/update/', views.blog_update),
  url(r'^blog/delete/(?P<blog_id>\d+)/$', views.blog_delete),
  url(r'^blog/detail/(?P<blog_id>\d+)/$', views.blog_detail),
  url(r'^blog/(?P<category>\w+)/$', views.blog_list),
  
  url(r'^auth/login/', views.auth_login),
  url(r'^auth/logout/', views.auth_logout),
  url(r'^auth/signup/', views.auth_signup),
]