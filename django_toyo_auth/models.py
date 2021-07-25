from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, verbose_name="UUID")
    student_id = models.CharField(max_length=10, default="", null=True, blank=True, verbose_name="学籍番号")
    entry_year = models.IntegerField(null=True, blank=True, verbose_name="入学年度")
    created_at = models.DateTimeField(default=timezone.localtime, verbose_name="作成日")
    is_student = models.BooleanField(default=False, verbose_name="学生か")

    class Meta:
        ordering = ["-created_at"]

    def get_school_year(self):
        if self.is_student:
            today = timezone.localdate()
            return today.year - self.entry_year + (1 if today.month > 3 else 2)
        else:
            return None
