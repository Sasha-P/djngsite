"""djngsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken import views as drf_views

from .views import SampleView, AngularApp
from .api import views as api_views

router = routers.DefaultRouter()

# ngurls = [
#     url(r'^$', SampleView.as_view(), name='sample'),
# ]

urlpatterns = [
    # url(r'^sample/', include(ngurls)),
    
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/user/auth/$', api_views.ObtainAuthToken.as_view()),
    url(r'^api/v1/user/reg/$', api_views.RegisterUserView.as_view()),
    url(r'^api/v1/user/$', api_views.UserProfile.as_view()),
    url(r'^api/v1/user/posts/$', api_views.UserPosts.as_view()),
    url(r'^api/v1/post/$', api_views.PostList.as_view()),
    url(r'^api/v1/post/search/(?P<query>.+)$', api_views.PostSearch.as_view()),
    url(r'^api/v1/post/search/$', api_views.PostSearch.as_view()),

    url(r'^api/v1/heroes/$', api_views.Heroes.as_view()),

    url(r'^(?!ng/).*$', AngularApp.as_view(), name='angular_app'),
] + static(settings.ANGULAR_URL, document_root=settings.ANGULAR_ROOT)
