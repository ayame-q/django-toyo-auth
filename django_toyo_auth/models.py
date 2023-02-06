from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser as DjangoAbstractUser
from django.utils import timezone


# Create your models here.
class AbstractUser(DjangoAbstractUser):
    student_id = models.CharField(max_length=10, default="", null=True, blank=True, verbose_name="学籍番号")
    entry_year = models.IntegerField(null=True, blank=True, verbose_name="入学年度")
    created_at = models.DateTimeField(default=timezone.localtime, verbose_name="作成日")
    is_student = models.BooleanField(default=False, verbose_name="学生か")
    is_toyo_member = models.BooleanField(default=False, verbose_name="東洋大学内者か")
    is_iniad_member = models.BooleanField(default=False, verbose_name="INIAD学内者か")
    _grade_gap = models.IntegerField(default=0, verbose_name="ストレートとの学年の差")

    class Meta:
        ordering = ["-created_at"]
        abstract = True

    @property
    def grade(self):
        if self.is_student:
            today = timezone.localdate()
            return today.year - self.entry_year + (1 if today.month > 3 else 0) + self._grade_gap
        else:
            return None

    @grade.setter
    def grade(self, grade):
        if self.grade != grade:
            today = timezone.localdate()
            self._grade_gap = grade - (today.year - self.entry_year + (1 if today.month > 3 else 0))

    grade.fget.short_description = "学年"

class UUIDAbstractUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, verbose_name="UUID")

    class Meta:
        ordering = ["-created_at"]
        abstract = True
