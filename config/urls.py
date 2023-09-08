"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

#!Django Modules
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _


#!Abstract
from abstract.constants import AppName
from abstract.views import *



# *Admin Site Configuration
admin.site.site_header = _("RentBook Admin")  # login page
admin.site.site_title = _("RentBook Admin User")  # html <title> tag
admin.site.index_title = _("Welcome My RentBook Project")  # site administration

urlpatterns = []

if not settings.APP_NAME or settings.APP_NAME not in [app.value for app in AppName]:
    raise Exception(_("Please set app correct name same as abstract.constants.AppName"))


urls_admin = [
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path("ckeditor/", include("ckeditor_uploader.urls")),  
]

if settings.APP_NAME == AppName.ADMIN.name:
    urlpatterns += urls_admin
else:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        path('',BookTitleListView.as_view(),name='home'),
        path('change/',changeTheme,name='change'),
        path("author/",include('apps.author.urls',namespace='author')),
        path("book/",include('apps.book.urls',namespace='book')),                                       
        path("customer/",include('apps.customer.urls',namespace='customer')),                                       
        path("publisher/",include('apps.publisher.urls',namespace='publisher')),
        path("rental/",include('apps.rental.urls',namespace='rental')),       
    ]
    urlpatterns += urls_admin
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))


# *Settings Debug
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
