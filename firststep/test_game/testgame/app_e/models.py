#encoding:utf8
from django.db import models

# Create your models here.
'''根据生日输入的测试题页面'''
class Exam_e(models.Model):
    exam_photo = models.FileField(upload_to='./exam_e')#测试游戏照片
    exam_topic = models.CharField(max_length=200)#测试游戏名
    exam_descript = models.TextField()#测试游戏描述
    exam_background_photo = models.FileField(upload_to='./exam_e')#测试游戏背景照片
    def __unicode__(self):
    	return self.exam_topic


'''结果'''
class Exam_option(models.Model):
    option_photo = models.FileField(upload_to='./exam_e_option')#结果照片
    option_topic = models.CharField(max_length=200)#结果名
    option_descript = models.TextField()#结果描述
    option_min = models.IntegerField()
    option_max = models.IntegerField()     
 
    exam = models.ForeignKey(Exam_e)
    def __unicode__(self):
    	return self.option_topic
