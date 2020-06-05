from . import views
from django.urls import path
from django.conf.urls.static import static

#determines the url link. Makes it pretties than www.gooogle.com/aedfsadsfasdfda/a/asd231e3/sas

urlpatterns=[
    path('', views.PostList.as_view(),name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 