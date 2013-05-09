#encoding:utf8
from django.db import models


'''星座测试页面'''
class Exam_c(models.Model):
    exam_topic = models.CharField(max_length=200)#测试游戏名字
    exam_photo = models.FileField(upload_to="./exam_c")#测试游戏照片

    def __unicode__(self):
        return self.exam_topic


'''返回结果'''
class Exam_c_question(models.Model):
    question_photo = models.FileField(upload_to="./exam_c_question")#具体题目照片
    option_photo = models.FileField(upload_to="./exam_c_option")#结果照片
    option_topic = models.CharField(max_length=200)#结果奖项名
    option_descript = models.TextField()#结果描述

    exam_c = models.ForeignKey(Exam_c)   #测试游戏外键
    def __unicode__(self):
        return self.option_topic


