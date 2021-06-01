from django.urls import path
from send_email_project import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'send_email_project'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('sendmail/', views.index, name='index_page'),
    path('email_sent/', views.email_sent, name='email_sent'),
]
