from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$',views.index,name='Index'),
    re_path(r'^notifications',views.notification, name='notifications'),
    re_path(r'^blog',views.blog, name='blog'),
    re_path(r'^health',views.health, name='health'),
    re_path(r'^authorities',views.authorities, name='authorities'),
    re_path(r'^businesses',views.businesses, name='businesses'),
    re_path(r'^view/blog/(\d+)',views.view_blog,name='view_blog'),
    re_path(r'^my-profile/',views.my_profile, name='my-profile'),
    re_path(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    re_path(r'^new/blogpost$',views.new_blogpost, name='new-blogpost'),
    re_path(r'^new/business$',views.new_business, name='new-business'),
    re_path(r'^create/profile$',views.create_profile, name='create-profile'),
    re_path(r'^new/notification$',views.new_notification, name='new-notification'),
    re_path(r'^update/profile$',views.update_profile, name='update-profile'),
    re_path(r'^search/',views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)