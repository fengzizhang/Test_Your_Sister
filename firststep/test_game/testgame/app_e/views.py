#coding:utf8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from app_e.models import *
import datetime

'''年月日输入测试主页'''
def exam_e(request):
    exams = Exam_e.objects.all()
    return render_to_response('exam_e.html',{'exams':exams})

'''具体测试页面'''
def exam_e_info(request,eid):
    today_year = datetime.datetime.now().year
    today_month = datetime.datetime.now().month
    today_day = datetime.datetime.now().day
    #print type(today_year)
    exam = Exam_e.objects.get(id=eid)
    all_days = 0
    exam_options = exam.exam_option_set.all()
    if request.method == 'POST':
    	time = request.POST['time']
        time = str(time)
        if len(time) == 0:
            return render_to_response('exam_e_info.html',{'exam':exam,'exam-options':exam_options})   
        else:    
            year = int(time[6:])
            month = int(time[0:2])
            day = int(time[3:5])
            #print type(year)
            #print type(time)
            year_num = today_year - year
            month_num = today_month - month
            day_num = today_day - day
    
            all_days = year_num*365 + month_num*30 + day_num
            print all_days
            return render_to_response('exam_e_info.html',{'exam':exam,'exam-options':exam_options,'all_days':all_days})







    
