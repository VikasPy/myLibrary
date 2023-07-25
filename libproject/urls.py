"""libproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libapp import views

urlpatterns =[
    path('13admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('home', views.home , name='home'),
    path('about', views.about , name='about'),
    path('courses', views.courses , name='courses'),
    path('login', views.login , name='login'),
    path('search', views.search , name='search'),
    path('searched_book/<int:id>', views.searched_book , name='searched_book'),
    path('logout', views.logout , name='logout'),
    path('signup', views.signup , name='signup'),
    path('profile_update', views.profile_update , name='profile_update'),
    path('profile_user', views.profile_user , name='profile_user'),
    path('book_read/<int:id>', views.book_read , name='book_read'),
    path("book_cat/<str:cat>",views.book_cat,name="book_cat"),
    path("pton_data/<str:topic>",views.pton_data,name="pton_data"),

    path("pton_start",views.pton_start,name="pton_start"),
    path('book_click', views.book_click , name='book_click'),
    path('contact_user', views.contact_user , name='contact_user'),
    path('comnt', views.comnt , name='comnt'),
    path('commenter<int:id>', views.commenter , name='commenter'),
    path("likepost",views.likepost,name="likepost"),
    path("delit_comment/<int:id>",views.delit_comment,name="delit"),
    
]
