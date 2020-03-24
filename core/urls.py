from . import views
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact/', views.ContactPage, name='contact'),
    path('guestbook/', views.GuestbookPage, name='guestbook'),
    path('penumbra/', views.PenumbraPage, name='penumbra'),
    path('success/', views.SuccessPage, name='success'),
    path('banana/', views.GiveBanana, name='banana'),
    path('access/', views.Login, name='access'),
    path('logout/', views.Logout, name='logout'),
    path('codex/<str:file>', views.CodexIndex, name='codex'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]