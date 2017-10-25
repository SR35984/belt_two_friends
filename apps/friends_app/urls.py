from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name= "landing"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^friends$', views.friends, name="dashboard"),
    url(r'^addfriend$', views.add_friend, name="add_friend"),
    url(r'^remfriend$', views.delete_friend, name="delete_friend"),
    url(r'^showuser/(?P<userid>[0-9]+)$', views.show_user, name="show_user"),
]