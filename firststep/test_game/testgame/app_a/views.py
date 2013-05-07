#encoding:utf8
from django.utils import simplejson as json
from app_a.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger



'''常识测试主页'''
def index(request):
    exams = Exam_a.objects.all()
    return render_to_response('index.html',locals())

'''具体测试页面'''
def exam_info(request,eid):
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

    p     = Paginator(questions,1)
    page  = request.GET.get('page')
    try:
        contacts = p.page(page)
    except PageNotAnInteger:
        contacts = p.page(1)
    except EmptyPage:
        contacts = p.page(paginator.num_pages)
    return render_to_response('exam_info.html',locals())
