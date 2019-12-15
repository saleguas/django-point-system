from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
    # ? = START
    # $ = END
    # (?P<slug>) named group
    # [\w-]

app_name = 'points'

urlpatterns = [
    path('', views.points_list, name="list"),
    path('entry/', views.points_entrys, name="point-entry-form"),
    path('<int:id>', views.points_detail, name="breakdown"),

]
