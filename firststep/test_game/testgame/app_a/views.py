#encoding:utf8
from django.utils import simplejson as json
from app_a.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger



'''常识测试主页'''
def exam_a(request):
    exams = Exam_a.objects.all()
    return render_to_response('exam_a.html',locals())

'''具体测试页面'''
def exam_a_info(request,eid):
    exam = Exam_a.objects.get(id=eid)
    questions = exam.exam_a_question_set.all()
    questions_list=[]
    for question in questions:
    	questions_list.append({
            'id':question.id, 
            'question_topic':question.question_topic,
            'a':question.a,
            'b':question.b,
            'c':question.c,
            'answer':question.answer,
            'ans':'' 
})    
    quest = json.dumps(questions_list)

    return render_to_response('exam_a_info.html',locals())
