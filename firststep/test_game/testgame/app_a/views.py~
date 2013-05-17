#encoding:utf8
from django.utils import simplejson as json
from app_a.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from weibo import APIClient, APIError
import weibo
import os
import sys
import webbrowser


APP_KEY = '3469247574'
APP_SECRET = 'd57bddcba8867095446ae0477b512cf6'
CALLBACK_URL = 'http://www.cenimei.com/index2'
client = weibo.APIClient(app_key=APP_KEY,app_secret=APP_SECRET,redirect_uri=CALLBACK_URL)

def index1(request):
    url = client.get_authorize_url()
    return render_to_response('index1.html',{'url':url})

def index2(request):
    code =request.GET.get('code')
    r = client.request_access_token(code)
    access_token = r.access_token
    espires_in = r.expires_in
    client.set_access_token(access_token,espires_in)
    request.session['token'] = access_token
    request.session['espires'] = espires_in
    print '====',request.session.get('k')
    uid = client.account.get_uid.get()
    id = uid['uid']  
    username = id
    email = str(id) + '@qq.com'
    password = id
    user = authenticate(username=id,password=id)
    if user is None:
        User.objects.create_user(username,email,password)
    #把用户存到django的用户中，并完成django用户登录
    #username = '按照规则生成用户名  uid'
    #user = User(username,)
    return HttpResponseRedirect('/index/')

import random
def index(request):
    access_token = request.session['token'] 
    espires_in = request.session['espires']
    client.set_access_token(access_token,espires_in)
    #print '*****',request.session.get('k')
    uid = client.account.get_uid.get()
    id = uid['uid']
    ur = client.users.show.get(uid=id)
    name = ur['name']
    headimg = ur['avatar_large']
    request.session['userinfo'] = {'name':name,'headimg':headimg}
    exams_a = Exam_a.objects.all()
    
    friends = client.friendships.friends.bilateral.ids.get(uid=id)
    #print friends
    ids = friends['ids']  
    
    #print ids   
    fr = []  
    for id1 in ids[0:5]:
       # print '======',id1
        try:
            fr.append(client.users.show.get(uid=id1))
        except APIError:
            pass
    request.session['fr'] = fr    	
    headimgs = [] 
    names = []   
    for fr1 in fr:
        headimgs.append(fr1['avatar_large'])
        #print '$$$$$$',headimgs
        names.append(fr1['name'])
        #print '######',names
    #print headimgs

    #print "************************",friends     
    request.session['headimg'] = headimgs
    request.session['name'] = names   	
   # exams_b = Exam_b.objects.all()
 #   exams_c = Exam_c.objects.all()
   # exams_d = Exam_d.objects.all()
  #  exams_e = Exam_e.objects.all()
    return render_to_response('index.html',locals())



def mylogout(request):
    request.session.get('k')
    client.account.end_session 
    logout(request)
    return HttpResponseRedirect('/index1')


'''常识测试主页'''
def exam_a(request):
    request.session.get('k')
    uid = client.account.get_uid.get()
    id = uid['uid']
    ur = client.users.show.get(uid=id)
    name = ur['name']
    #email = client.account.profile.email.get()
    #eml = email['email']
    headimg = ur['avatar_large']
    exams = Exam_a.objects.all()
    return render_to_response('exam_a.html',locals())

'''具体测试页面'''
import os
def exam_a_info(request,eid):
    request.session.get('k')
    uid = client.account.get_uid.get()
    id = uid['uid']
    ur = client.users.show.get(uid=id)
    name = ur['name']
    #email = client.account.profile.email.get()
    #eml = email['email']
    headimg = ur['avatar_large']
    exam = Exam_a.objects.get(id=eid)
    questions = exam.exam_a_question_set.all()
    options = exam.exam_option_set.all()
    questions_list=[]
    for question in questions:
        questions_list.append({
            'id':question.id - (int(eid)-1)*5, 
            'question_topic':question.question_topic,
            'a':question.a,
            'b':question.b,
            'c':question.c,
            'answer':question.answer,
            'ans':'' 
})    
    quest = json.dumps(questions_list)
    options_list=[]
    for option in options:
        photo_name = os.path.basename(option.option_photo.name)
        photo_name = os.path.join('static', 'option_a_photo', photo_name)
        print photo_name
        options_list.append({
            'option_photo':photo_name,
            'id':option.id,
            'option_topic':option.option_topic,
            'option_descript':option.option_descript,
            'score_min':option.score_min,
            'score_max':option.score_max
})
    opt = json.dumps(options_list)
    return render_to_response('exam_a_info.html',locals())
