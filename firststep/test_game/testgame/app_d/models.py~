#encoding:utf8
from django.db import models

# Create your models here.
'''开心测试页面'''
class Exam_d(models.Model):
    exam_topic = models.CharField(max_length=200)#测试游戏名
    exam_photo = models.FileField(upload_to="./exam_d_photo")#测试游戏照片
    exam_picture = models.FileField(upload_to="./exam_d_picture")#测试游戏图片
    exam_descript = models.TextField()#测试游戏描述
    def __unicode__(self):
    	return self.exam_topic
'''返回结果'''
class Exam_option(models.Model):
    option_topic = models.CharField(max_length=200)#结果奖项名
    option_photo = models.FileField(upload_to="./exam_d_option")#结果图片
    option_descript = models.TextField()#结果描述
    
    exam_d = models.ForeignKey(Exam_d)#测试游戏外键
    def __unicode__(self):
    	return self.option_topic
