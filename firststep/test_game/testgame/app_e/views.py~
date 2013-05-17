#coding:utf8
from django.utils import simplejson as json
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from app_e.models import *
import datetime

'''年月日输入测试主页'''
def exam_e(request):
    userinfo = request.session['userinfo']
    name = userinfo['name']
    headimg = userinfo['headimg'] 
    exams = Exam_e.objects.all()
    return render_to_response('exam_e.html',{'exams':exams,'headimg':headimg,'name':name})

'''具体测试页面'''
import os
def exam_e_info(request,eid):
    userinfo = request.session['userinfo']
    name = userinfo['name']
    headimg = userinfo['headimg'] 
    exam = Exam_e.objects.get(id=eid)
    exam_options = exam.exam_option_set.all()
    options_list = []
    for option in exam_options:
        print option.option_photo
        photo_name = os.path.basename(option.option_photo.name)
        photo_name = os.path.join('static', 'exam_e_option', photo_name)
    	options_list.append({
            'id':option.id,
            'option_photo':photo_name,
            'option_topic':option.option_topic,
            'option_descript':option.option_descript,
            'option_min':option.option_min,  
            'option_max':option.option_max
})
    opt = json.dumps(options_list)
    return render_to_response('exam_e_info.html',{'exam':exam,'opt':opt,'exam_options':exam_options,'headimg':headimg,'name':name})







    
