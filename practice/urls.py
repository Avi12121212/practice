"""practice URL Configuration

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
from django.urls import path, include

# import practiceApp
from . import views

urlpatterns = [
    path("", views.home),
    path('admin/', admin.site.urls),
    path("book/", views.books),
    # path("result/",views.result),
    path("radio/", views.radio),
    path("api/", views.api),
    path("getdata/", views.getdata),
    path("test/", views.test),
    path("quiz/", views.quiz),
    path("apiquiz/", views.apiquiz),
    path("session/",views.session),
    path("sessionview/",views.sessionview),
    path("sessionremove/", views.sessionremove)
]
