#encoding:utf8
# Create your views here.
from app_b.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from weibo import APIClient, APIError
import weibo
import os
import sys
import webbrowser


'''星座测试主页'''
def exam_b(request):
    userinfo = request.session['userinfo']
    name = userinfo['name']
    headimg = userinfo['headimg']    
    exams = Exam_b.objects.all()
    return render_to_response('exam_b.html',{'exams':exams,'headimg':headimg,'name':name})

'''具体测试页面'''
import random
def exam_b_info(request,eid):
    names = request.session['name']    
    headimgs = request.session['headimg']
    #friends_info = request.session['friends_info'] 
    #print '++++',friends   
    userinfo = request.session['userinfo']
    name = userinfo['name']
    headimg = userinfo['headimg']
   
    exam = Exam_b.objects.get(id=eid)
    exam_options = exam.exam_option_set.all()
    exam_option = random.choice(exam_options)
    if request.method == 'POST':
        title = request.POST['title']
        print title 
    return render_to_response('exam_b_info.html',{'exam_option':exam_option,'exam':exam,'headimg':headimg,'name':name,'headimgs':headimgs,'names':names})

APP_KEY = '3469247574'
APP_SECRET = 'd57bddcba8867095446ae0477b512cf6'
CALLBACK_URL = 'http://www.b.com/index2'
client = weibo.APIClient(app_key=APP_KEY,app_secret=APP_SECRET,redirect_uri=CALLBACK_URL)

from django import http
def fa_wei(request):
    access_token = request.session['token'] 
    espires_in = request.session['espires']
    client.set_access_token(access_token,espires_in)
    
    #print request.session.get('k')
    if request.method == 'POST':
        fenxiang = request.POST['fenxiang']
        #print fenxiang
        img = request.POST['img']
        print 'img=',img
    fr = request.session['fr']
    for ff in fr:
        #print 'ff=',ff
        if ff['avatar_large'] == img:
            name = ff['name']
            print 'name=',name
            client.statuses.update.post(status=fenxiang+' '+'@'+name)            
    return http.HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))        	        
'''
def exam_c_score(request,eid,uid):
    exam = Exam_c.objects.get(id=eid)
    questions = exam.exam_c_question_set.all()
    quest = Exam_c_question.objects.get(id=uid)
    return render_to_response('exam_c_info.html',locals())
#结果页

def exam_c_score(request,eid):
    question = Exam_c_question.objects.get(id=eid)
    return render_to_response('exam_c_score.html',locals())
'''
