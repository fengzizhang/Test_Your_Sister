#coding:utf8
from django.db import models

'''常识测试'''
class Exam_a(models.Model):
    exam_topic = models.CharField(max_length=200) #测试游戏名字
    exam_descript = models.TextField()   #测试游戏描述
    exam_photo = models.FileField(upload_to='./exam_a_photo') #测试游戏照片
    exam_picture = models.FileField(upload_to='./exam_a_picture') #测试游戏图片
   
    def __unicode__(self):
    	return self.exam_topic

'''题目选项'''
class Exam_a_question(models.Model):
    question_topic = models.CharField(max_length=200)  #具体题目名
    a = models.CharField(max_length=200) #题目选项
    b = models.CharField(max_length=200) 
    c = models.CharField(max_length=200) 
    answer = models.CharField(max_length=2)    #题目答案

    exam_a = models.ForeignKey(Exam_a)    #测试游戏外键

    def __unicode__(self):
    	return self.question_topic


'''返回结果'''
class Exam_option(models.Model):
    option_photo = models.FileField(upload_to='./option_a_photo')
    option_topic = models.CharField(max_length=200) #结果奖项名
    option_descript = models.TextField()    #结果描述
    score_min = models.IntegerField()  #游戏分数段最小值
    score_max = models.IntegerField()  #游戏分数段最大值
    #score = models.IntegerField(default=0)  #游戏所得分数    

    exam_a = models.ForeignKey(Exam_a)  #测试游戏外键

    def __unicode__(self):
    	return self.option_topic	







