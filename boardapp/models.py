import re

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models



# Create your models here.
from courseapp.models import Course



class Board(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='board', null=True)
    title = models.CharField(max_length=200, null=True)
    content = RichTextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    type_choice = [('notice',  '공지사항'), ('data', '강의자료'), ('board', '토론게시판')]
    type = models.CharField(max_length=10, choices=type_choice, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='board', null=True)
    # course_id = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course', null=True)
    #def summary(self):
    #    if len(self.content) > 200:
    #        return self.content[:200] + ' ...'



    def summary(self):
        remove_tags = re.compile('<.*?>')
        if len(re.sub(remove_tags, '', self.content)) > 100:
            return re.sub(remove_tags, '', self.content)[:100] + ' ...'
        return re.sub(remove_tags, '', self.content)

    # def summary_preview_title(self):
    #     remove_tags = re.compile('<.*?>')
    #     return re.sub(remove_tags, '', self.title)[:10]
    #
    # def summary_preview_content(self):
    #     remove_tags = re.compile('<.*?>')
    #     if len(re.sub(remove_tags, '', self.content)) > 15:
    #         return re.sub(remove_tags, '', self.content)[:15] + '\n' + re.sub(remove_tags, '', self.content)[15:30]
    #
    #     return re.sub(remove_tags, '', self.content)
