import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
# 创建问题模型
class Question(models.Model):

    # 修复模型输出问题
    def __str__(self):
        return self.question_text

    # 添加一个自定义方法
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # 添加问题主键
    question_id = models.BigAutoField(primary_key=True, db_comment="问题主键")
    # 添加问题内容
    question_text = models.CharField(max_length=200, db_comment="问题")
    # 添加问题发布时间
    pub_date = models.DateTimeField("date published", db_comment="发布时间")


# 创建选项模型
class Choice(models.Model):

    # 修复模型输出问题
    def __str__(self):
        return self.choice_text
    # 添加选项主键
    choice_id = models.BigAutoField(primary_key=True, db_comment="选项主键")
    # 添加选项关联问题
    question = models.ForeignKey(Question, on_delete=models.CASCADE, db_comment="问题关联")
    # 添加选项内容
    choice_text = models.CharField(max_length=200, db_comment="选项")
    # 添加选项票数
    votes = models.IntegerField(default=0, db_comment="投票数")
