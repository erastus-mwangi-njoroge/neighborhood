from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path(r'^$',views.index,name='Index'),
    path(r'^notifications',views.notification, name='notifications'),
    path(r'^blog',views.blog, name='blog'),
    path(r'^health',views.health, name='health'),
    path(r'^authorities',views.authorities, name='authorities'),
    path(r'^businesses',views.businesses, name='businesses'),
    path(r'^view/blog/(\d+)',views.view_blog,name='view_blog'),
    path(r'^my-profile/',views.my_profile, name='my-profile'),
    path(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    path(r'^new/blogpost$',views.new_blogpost, name='new-blogpost'),
    path(r'^new/business$',views.new_business, name='new-business'),
    path(r'^create/profile$',views.create_profile, name='create-profile'),
    path(r'^new/notification$',views.new_notification, name='new-notification'),
    path(r'^update/profile$',views.update_profile, name='update-profile'),
    path(r'^search/',views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)