from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from points.sitemaps import *
from django.conf.urls.static import static
from django.conf import settings

sitemaps = {
    'student' : StudentSitemap,
    'MeetingEntry' : MeetingEntryMap,
    'static' : StaticViewSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('points/', include('points.urls')),
    path('', views.index, name='main'),
    path('gallery/', views.gallery, name='gallery'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetings/<int:pk>', views.meetings_detail, name="meetingList"),
    path('BingSiteAuth.xml', views.bingAuth),
    path('google225f06044a247783.html', views.googleAuth)

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
