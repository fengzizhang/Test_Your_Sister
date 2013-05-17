#encoding:utf8
# Create your views here.
from app_c.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
'''星座测试主页'''
def exam_c(request):
    userinfo = request.session['userinfo']
    name = userinfo['name']
    headimg = userinfo['headimg'] 
    exams = Exam_c.objects.all()
    print exams
    return render_to_response('exam_c.html',{'exams':exams,'request':request,'headimg':headimg,'name':name})

'''具体测试页面'''

def exam_c_info(request,eid):
    userinfo = request.session['userinfo']
    name = userinfo['name']
    headimg = userinfo['headimg'] 
    exam = Exam_c.objects.get(id=eid)
    questions = exam.exam_c_question_set.all()
    quest = Exam_c_question.objects.get(id=eid)
    return render_to_response('exam_c_info.html',locals())
