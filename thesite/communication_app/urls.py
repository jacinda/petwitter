from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()


from communication_app import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^new_pet/$', views.new_pet, name='new_pet'),
    url(r'^profiles/(\d+)$', views.profile, name='profile'),
    url(r'^update/(.+)$', views.update, name='update'),
    url(r'^set_description/(\d+)', views.set_description, name='set_description'),
    url(r'^delete_my_pets/', views.delete_my_pets, name='delete_my_pets'),
)
