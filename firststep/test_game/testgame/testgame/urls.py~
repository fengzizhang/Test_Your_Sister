#coding:utf8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testgame.views.home', name='home'),
    # url(r'^testgame/', include('testgame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/$','app_a.views.index'),
    url(r'^index1/$','app_a.views.index1'),
    url(r'^index2/$','app_a.views.index2'),
    url(r'^logout/$','app_a.views.mylogout'),

    url(r'^exam_a/$','app_a.views.exam_a'),  #常识测试
    url(r'^exam_a_info/(?P<eid>\d+)/$','app_a.views.exam_a_info'),
    url(r'^fa_wei/$','app_b.views.fa_wei'),

    url(r'^exam_b/$','app_b.views.exam_b'),  #常识测试
    url(r'^exam_b_info/(?P<eid>\d+)/$','app_b.views.exam_b_info'),
    
    url(r'^exam_c/$','app_c.views.exam_c'), #星座测试
    url(r'^exam_c_info/(?P<eid>\d+)/$','app_c.views.exam_c_info'),

    url(r'^exam_e/$','app_e.views.exam_e'), #输入年月日测试
    url(r'^exam_e_info/(?P<eid>\d+)/$','app_e.views.exam_e_info'),

   
)
