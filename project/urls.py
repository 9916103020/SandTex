from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
               url(r'^$', views.home),
               url(r'^home/$', views.home, name='home'),
               url(r'^about/$', views.about, name='about'),
               url(r'^register/$', views.register, name='register'),
               url(r'^login/$', LoginView.as_view(template_name="accounts/login.html"), name='login'),
               url(r'^logout/$', LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
               url(r'choice/$',views.choice),
               url(r'^editor/$',views.editor,name='editor'),
               url(r'^compile/$',views.compile,name='compile'),
               url(r'^pdf/$',views.pdf_viewer,name='pdf'),
#               url(r'^save/$',views.savetex,name='save'),
               url(r'^save/$',views.my_code,name='save'),
               ]
