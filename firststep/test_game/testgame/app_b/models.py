#coding:utf8
from django.db import models

# Create your models here.
 
 #友趣测试页面
class Exam_b(models.Model):
    exam_topic = models.CharField(max_length=200)#测试游戏名
    exam_photo = models.FileField(upload_to="./exam_b_photo")#测试游戏照片
    exam_picture = models.FileField(upload_to="./exam_b_picture")#测试游戏图
 
    exam_descript = models.TextField()#测试游戏描述
    def __unicode__(self):
    	return self.exam_topic
 #返回结果
class Exam_option(models.Model):
    option_sex = models.CharField(max_length=200)#判定男女用户
    option_topic = models.CharField(max_length=200)#结果奖项名
    option_photo = models.FileField(upload_to="./exam_b_option")#结果图片
    option_descript = models.TextField()#结果描述
  
    exam_b = models.ForeignKey(Exam_b)#测试游戏外键
    def __unicode__(self):
    	return self.option_topic
