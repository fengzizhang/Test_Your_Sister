#coding:utf8
# Create your views here.
from app_d.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
'''星座测试主页'''
def exam_d(request):
    exams = Exam_d.objects.all()
    return render_to_response('exam_d.html',locals())

'''具体测试页面'''
def exam_d_info(request,eid):
    exam = Exam_d.objects.get(id=eid)
    questions = exam.exam_d_question_set.all()
    return render_to_response('exam_d_info.html',locals())
#结果页
def exam_d_score(request,eid):
    question = Exam_option.objects.get(id=eid)
    return render_to_response('exam_d_score.html',locals())
