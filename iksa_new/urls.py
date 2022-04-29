"""iksa_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from sitehandler.views import *

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('acservicebooking/',acservicebooking,name='acservicebooking'),
    path('login_user/',login_user,name='login_user'),
    path('adminlogin/',adminhome,name='adminhome'),
    path('logout_user/',logout_user,name='logout_user'),
    # Admin Paths
    path('admin_skaters_outsiders/',admin_skaters_outsiders,name='admin_skaters_outsiders'),
    path('admin_skaters_insiders/',admin_skaters_insiders,name='admin_skaters_insiders'),
    path('admin_dancer_insiders/',admin_dancer_insiders,name='admin_dancer_insiders'),
    path('admin_dancer_outsiders/',admin_dancer_outsiders,name='admin_dancer_outsiders'),
    path('admin_ac_services/',admin_ac_services,name='admin_ac_services'),
    path('skater_registration/',skater_registration,name='skater_registration'),
    path('dancer_registration/',dancer_registration,name='dancer_registration'),
    # Skating Coach paths
    path('skating_coach_login/',skating_coach_login,name='skating_coach_login'),
    path('skating_coach_outsiders/',skating_coach_outsiders,name='skating_coach_outsiders'),
    path('skating_coach_sendto_insider<int:pid>',skating_coach_sendto_insider,name='skating_coach_sendto_insider'),
    path('skating_coach_insiders/',skating_coach_insiders,name='skating_coach_insiders'),
    path('skating_coach_sendto_outsider<int:pid>',skating_coach_sendto_outsider,name='skating_coach_sendto_outsider'),
    path('skating_coach_delete<int:pid>',skating_coach_delete,name='skating_coach_delete'),
    # Dance Choreagraphers paths
    path('dance_choreographer_login/',dance_choreographer_login,name='dance_choreographer_login'),
    path('dance_choreographer_insiders/',dance_choreographer_insiders,name='dance_choreographer_insiders'),
    path('dance_choreographer_outsiders/',dance_choreographer_outsiders,name='dance_choreographer_outsiders'),
    path('dance_choreographer_sendto_insider<int:pid>',dance_choreographer_sendto_insider,name='dance_choreographer_sendto_insider'),
    path('dance_choreographer_sendto_outsider<int:pid>',dance_choreographer_sendto_outsider,name='dance_choreographer_sendto_outsider'),
    path('dance_choreographer_delete<int:pid>',dance_choreographer_delete,name='dance_choreographer_delete'),
    # AC Service paths
    path('ac_service_login/',ac_service_login,name='ac_service_login'),
    path('ac_service_pending/',ac_service_pending,name='ac_service_pending'),
    path('ac_service_done/',ac_service_done,name='ac_service_done'),
    path('ac_service_sendto_done<int:pid>',ac_service_sendto_done,name='ac_service_sendto_done'),
    path('ac_service_sendto_pending<int:pid>',ac_service_sendto_pending,name='ac_service_sendto_pending'),
    path('ac_service_delete<int:pid>',ac_service_delete,name='ac_service_delete'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
